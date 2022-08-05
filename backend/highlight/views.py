from pygments.formatters.terminal256 import Terminal256Formatter
from pygments.formatters.terminal import TerminalFormatter
from pygments.formatters.bbcode import BBCodeFormatter
from pygments.formatters.other import NullFormatter
from pygments.formatters.html import HtmlFormatter
from pygments.formatters.irc import IRCFormatter
from pygments.formatters.rtf import RtfFormatter
from pygments.formatters.svg import SvgFormatter
from rest_framework.permissions import AllowAny
# from pygments.formatters.img import (
#     JpgImageFormatter, BmpImageFormatter,
#     ImageFormatter, GifImageFormatter,
# )
from .serializers import HighlighterSerializer
from pygments.lexers import get_lexer_by_name, get_all_lexers
from pygments.styles import get_style_by_name, get_all_styles
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework import status
from pygments import highlight


class Highlighter(APIView):
    """
    Highlighter API
    """
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        """
        Takes a code snippet, returns the highlighted code.
        """
        serializer = HighlighterSerializer(data=request.data, context={'request': request})
        
        # if the serializer is valid, run this statement.
        if serializer.is_valid():
            code = serializer.validated_data.get('code')
            lexer = get_lexer_by_name(serializer.validated_data.get('language'))
            style = get_style_by_name(serializer.validated_data.get('style'))
            getFormat: str = serializer.validated_data.get('getFormat')

            #---more options, for formatters that require this settings.

            # linenos is used to determine if the result should have line numbers
            # activated or not, this can be one of ['inline', 'table', 'none'],
            # NOTE: 'none' is converted to False over here, default is False.
            linenos = False if serializer.validated_data.get('lineNos') == 'none' else serializer.validated_data.get('lineNos')
            
            # HTML: noclasses is used to determine if the user requires inline css
            # styling or css classes, if the css serializer data is 'inline', it
            # then means True for inline css styling else if the css data is 'class'
            # it then means False for 'inline' and True for 'class' styling.
            noclasses = True if serializer.validated_data.get('css') == 'inline' else False
            
            # HTML: class name to wrap the whole code block, defaults to highlighter,
            # NOTE: if linenos is set to table the cssclass name will append a 
            # 'table' making it 'highlightertable'.
            cssclass: str = serializer.validated_data.get('divClass')

            # Specify a list of lines to be highlighted in your result.
            hl_lines: list = serializer.validated_data.get('hlLines')
            
            # should the style selected also affect the overall code background?
            # defaults to False.
            nobackground: bool = serializer.validated_data.get('noBackground')

            # HTML: prefix the css classes used when 'noclasses' is set to 'class'
            # which means False for 'inline' styling and True for 'class' styling
            classprefix: str = serializer.validated_data.get('classPrefix')

            # custom inline css styles to insert into the div container
            # holding the main code snippet. NOTE: this is not gotten
            # from the serializer data, it is hard-coded.
            cssstyles: str = 'padding: 20px; width: 100rem;'
            
            # full is used to define if the user requires a full html
            # document, defaults to False
            # full: bool = serializer.validated_data.get('full')
            
            # the title of the html document if full is set to True
            # title: str = serializer.validated_data.get('title')

            # separate is used along side 'full' argument to request a separate
            # css style result and a body result, default to False
            # separate: bool = serializer.validated_data.get('separate')
            

            # which formatter was selected by the user?
            if getFormat.lower() in ['bbcode', 'bb']:
                formatter = BBCodeFormatter(style=style, codetag=True, monofont=True)
                highlighted = highlight(code, lexer, formatter)
                data = {
                    'status': 'success',
                    'result': {'highlighted': highlighted, 'sourcecode': getFormat.lower(), 'formatting': lexer.name}
                }
                return Response(data, status=status.HTTP_200_OK)

            elif getFormat.lower() in ['html', 'htm']:
                if noclasses:
                    # this means the user requested for an inline styling
                    formatter = HtmlFormatter(
                        style=style, linenos=linenos, noclasses=noclasses,
                        wrapcode=False, nobackground=nobackground, cssclass=cssclass,
                        hl_lines=hl_lines, cssstyles=cssstyles, lineseparator='<br>',
                    )
                    highlighted = highlight(code, lexer, formatter)
                    data = {
                        'status': 'success',
                        'result': {'highlighted': highlighted, 'sourcecode': getFormat.lower(), 'formatting': lexer.name}
                    }

                else:
                    # this means the user requested for class styling
                    formatter = HtmlFormatter(
                        style=style, linenos=linenos, noclasses=noclasses,
                        wrapcode=False, nobackground=nobackground, cssclass=cssclass,
                        hl_lines=hl_lines, cssstyles=cssstyles, lineseparator='<br>',
                        classprefix=classprefix,
                    )
                    highlighted = highlight(code, lexer, formatter)
                    styles = formatter.get_style_defs(F".{cssclass}")
                    data = {
                        'status': 'success',
                        'result': {'highlighted': highlighted, 'styles': styles, 'sourcecode': getFormat.lower(), 'formatting': lexer.name}
                    }
                return Response(data, status=status.HTTP_200_OK)

            elif getFormat.lower() in ['irc']:
                formatter = IRCFormatter(bg='dark', linenos=linenos)
                highlighted = highlight(code, lexer, formatter)
                data = {
                    'status': 'success',
                    'result': {'highlighted': highlighted, 'sourcecode': getFormat.lower(), 'formatting': lexer.name}
                }
                return Response(data, status=status.HTTP_200_OK)

            elif getFormat.lower() in ['rtf']:
                formatter = RtfFormatter(style=style, fontsize=28)
                highlighted = highlight(code, lexer, formatter)
                data = {
                    'status': 'success',
                    'result': {'highlighted': highlighted, 'sourcecode': getFormat.lower(), 'formatting': lexer.name}
                }
                return Response(data, status=status.HTTP_200_OK)

            elif getFormat.lower() in ['svg']:
                if linenos != False:
                    linenos = True

                formatter = SvgFormatter(
                    style=style, nowrap=False, fontfamily='monospace',
                    fontsize='16px', linenos=linenos, xoffset='20', yoffset="40"
                )
                highlighted = highlight(code, lexer, formatter)
                data = {
                    'status': 'success',
                    'result': {'highlighted': highlighted, 'sourcecode': getFormat.lower(), 'formatting': lexer.name}
                }
                return Response(data, status=status.HTTP_200_OK)

            elif getFormat.lower() in ['txt', 'text', 'null']:
                formatter = NullFormatter()
                highlighted = highlight(code, lexer, formatter)
                data = {
                    'status': 'success',
                    'result': {'highlighted': highlighted, 'sourcecode': getFormat.lower(), 'formatting': lexer.name}
                }
                return Response(data, status=status.HTTP_200_OK)
            
            # the terminal formatters should only be used while in terminal interfaces
            elif getFormat.lower() in ['terminal256', 'console256', '256']:
                formatter = Terminal256Formatter(style=style)
                highlighted = highlight(code, lexer, formatter)
                data = {
                    'status': 'success',
                    'result': {'highlighted': highlighted, 'sourcecode': getFormat.lower(), 'formatting': lexer.name}
                }
                return Response(data, status=status.HTTP_200_OK)

            elif getFormat.lower() in ['terminal', 'console']:
                formatter = TerminalFormatter(bg='dark', colorscheme=None, linenos=linenos)
                highlighted = highlight(code, lexer, formatter)
                data = {
                    'status': 'success',
                    'result': {'highlighted': highlighted, 'sourcecode': getFormat.lower(), 'formatting': lexer.name}
                }
                return Response(data, status=status.HTTP_200_OK)

            else:
                # if all is not well(error) run this code block statement.
                data = {
                    'status': 'failed',
                    'result': {'data' : None}
                }
                return Response(data, status=status.HTTP_404_NOT_FOUND)

        # else if the serializer is not valid run this statement.
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Options(APIView):
    """
    Options API
    """
    languages = sorted([lexer[0].lower() for lexer in get_all_lexers()])
    styles = sorted([style for style in get_all_styles()])
    formats = sorted(['bbcode', 'html', 'irc', 'rtf', 'svg', 'text', 'terminal', 'terminal256'])

    def get(self, request, option=None):
        # We made use of 'str' url kwargs so as to capture the type
        # of option the user is requesting, and then return the
        # appropriate result these can be one of
        # ['languages', 'styles', 'formats'].

        if option == "languages":
            return Response(data={"result": self.languages}, status=status.HTTP_200_OK )
        
        elif option == "formats":
            return Response(data = {"result": self.formats}, status=status.HTTP_200_OK )
        
        elif option == "styles":
            return Response(data = {"result": self.styles}, status=status.HTTP_200_OK )
        else:
            return Response(data={"detail": "error"}, status=status.HTTP_404_NOT_FOUND)


class APIRoot(APIView):
    """
    API Root View.
    """
    def get(self, request, format=None):
        data = {
            "Highlighter": reverse("highlighter:highlight", request=request, format=format),
            "Options": {
                "Styles": reverse("highlighter:highlight-options", request=request, format=format, args=['styles']),
                "Formats": reverse("highlighter:highlight-options", request=request, format=format, args=['formats']),
                "Languages": reverse("highlighter:highlight-options", request=request, format=format, args=['languages']),
            }
        }
        return Response(data, status=status.HTTP_200_OK)

