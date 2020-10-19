from pygments.formatters.terminal256 import Terminal256Formatter
from pygments.formatters.terminal import TerminalFormatter
from pygments.formatters.bbcode import BBCodeFormatter
from pygments.formatters.other import NullFormatter
from pygments.formatters.html import HtmlFormatter
from pygments.formatters.irc import IRCFormatter
from pygments.formatters.rtf import RtfFormatter
from pygments.formatters.svg import SvgFormatter
from rest_framework.permissions import AllowAny
from pygments.formatters.img import (
    JpgImageFormatter, BmpImageFormatter,
    ImageFormatter, GifImageFormatter,
)
from .serializers import HighlighterSerializer
from pygments.lexers import get_lexer_by_name, get_all_lexers
from pygments.styles import get_style_by_name, get_all_styles
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework import status
from pygments import highlight

# create class api
class Highlighter(APIView):
    """
    Class API view.
    does not have an queryset attribute. And makes use of the pygments
    python library.

    post:
    only allows post request along side the data(code text) to highlight.
    """
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = HighlighterSerializer(data=request.data, context={'request': request})
        
        # if the serializer is valid, run this statement.
        if serializer.is_valid():
            code: str = serializer.data.get('code')
            lexer = get_lexer_by_name(serializer.data.get('language'))
            style = get_style_by_name(serializer.data.get('style'))
            getFormat: str = serializer.data.get('getFormat')

            #---more options, for formatters that require this settings.
            # linenos is used to request if the result should have line numbers
            # or not, this can be one of ['inline', 'table', False], defaults to
            # False, no line numbers
            linenos = False if serializer.data.get('lineNos') == 'none' else serializer.data.get('lineNos')
            
            # noclasses is used to define if the user requires inline css
            # styling or classes, if set to True inline styling is used and
            # the 'full, separate and other optional arguments will not take
            # effect, defaults to True
            noclasses = True if serializer.data.get('styling') == 'inline' else False
            
            # class name to wrap the whole code block, defaults to highlighter,
            # NOTE: if linenos is set to table the cssclass name will append a 
            # 'table' making it 'highlightertable'.
            cssclass: str = serializer.data.get('divClass')

            # Specify a list of lines to be highlighted in your result.
            hl_lines: list = serializer.data.get('hlLines')
            
            # should the style selected also affect the overall code background?
            # defaults to False.
            nobackground: bool = serializer.data.get('noBackground')
            
            # full is used to define if the user requires a full html
            # document, defaults to False
            # full: bool = serializer.data.get('full')
            
            # the title of the html document if full is set to True
            # title: str = serializer.data.get('title')

            # separate is used along side 'full' argument to request a separate
            # css style result and a body result, default to False
            # separate: bool = serializer.data.get('separate')
            
            # prefix the css classes used when 'noclasses' is set to False
            classprefix: str = serializer.data.get('classPrefix')
     

            # which formatter was selected by the user?
            if getFormat.lower() in ['bbcode', 'bb']:
                formatter = BBCodeFormatter(style=style, codetag=True, monofont=True)
                highlighted = highlight(code, lexer, formatter)
                data = {
                    'status': 'success',
                    'result': {'data': highlighted}
                }
                return Response(data, status=status.HTTP_200_OK)

            elif getFormat.lower() in ['html', 'htm']:
                if noclasses:
                    formatter = HtmlFormatter(
                        style=style, linenos=linenos, noclasses=noclasses,
                        wrapcode=True, nobackground=nobackground, cssclass=cssclass,
                        hl_lines=hl_lines, lineseparator='<br>',
                    )
                    highlighted = highlight(code, lexer, formatter)
                    data = {
                        'status': 'success',
                        'result': {'data': highlighted}
                    }

                else:
                    formatter = HtmlFormatter(
                        style=style, linenos=linenos, noclasses=noclasses,
                        wrapcode=True, nobackground=nobackground, cssclass=cssclass,
                        hl_lines=hl_lines, lineseparator='<br>', classprefix=classprefix,
                    )
                    highlighted = highlight(code, lexer, formatter)
                    styles = formatter.get_style_defs(F".{cssclass}")
                    data = {
                        'status': 'success',
                        'result': {'data': highlighted, 'styles': styles}
                    }
                return Response(data, status=status.HTTP_200_OK)

            elif getFormat.lower() in ['irc']:
                formatter = IRCFormatter(bg='dark', linenos=linenos)
                highlighted = highlight(code, lexer, formatter)
                data = {
                    'status': 'success',
                    'result': {'data': highlighted}
                }
                return Response(data, status=status.HTTP_200_OK)

            elif getFormat.lower() in ['rtf']:
                formatter = RtfFormatter(style=style, fontsize=28)
                highlighted = highlight(code, lexer, formatter)
                data = {
                    'status': 'success',
                    'result': {'data': highlighted}
                }
                return Response(data, status=status.HTTP_200_OK)

            elif getFormat.lower() in ['svg']:
                formatter = SvgFormatter(
                    style=style, nowrap=False, fontfamily='monospace',
                    fontsize='16px', linenos=linenos,
                )
                highlighted = highlight(code, lexer, formatter)
                data = {
                    'status': 'success',
                    'result': {'data': highlighted}
                }
                return Response(data, status=status.HTTP_200_OK)

            elif getFormat.lower() in ['txt', 'text', 'null']:
                formatter = NullFormatter()
                highlighted = highlight(code, lexer, formatter)
                data = {
                    'status': 'success',
                    'result': {'data': highlighted}
                }
                return Response(data, status=status.HTTP_200_OK)
            
            # the terminal formatters should only be used while in terminal interfaces
            elif getFormat.lower() in ['terminal256', 'console256', '256']:
                formatter = Terminal256Formatter(style=style)
                highlighted = highlight(code, lexer, formatter)
                data = {
                    'status': 'success',
                    'result': {'data': highlighted}
                }
                return Response(data, status=status.HTTP_200_OK)

            elif getFormat.lower() in ['terminal', 'console']:
                formatter = TerminalFormatter(bg='dark', colorscheme=None, linenos=linenos)
                highlighted = highlight(code, lexer, formatter)
                data = {
                    'status': 'success',
                    'result': {'data': highlighted}
                }
                return Response(data, status=status.HTTP_200_OK)

                # if all is not well(error) run this code block statement.
            else:
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
    Class based API view to get all highlighter opotions.

    get:
    only allows get method.
    """
    languages = sorted([lexer[0].lower() for lexer in get_all_lexers()])
    styles = sorted([style for style in get_all_styles()])
    formats = sorted(['bbcode', 'html', 'irc', 'rtf', 'svg', 'text', 'terminal', 'terminal256'])

    def get(self, request, option=None, format=None):
        if option in ['language', 'languages']:
            data = {"result": self.languages}
            return Response(data, status=status.HTTP_200_OK )
        
        elif option in ['format', 'formats']:
            data = {"result": self.formats}
            return Response(data, status=status.HTTP_200_OK )
        
        elif option in ['style', 'styles']:
            data = {"result": self.styles}
            return Response(data, status=status.HTTP_200_OK )
        
        else:
            return Response({"result" : {"data": "error"}}, status=status.HTTP_404_NOT_FOUND)


class APIRoot(APIView):
    """
    Class based api root view, returns the urls available for access.
    """
    def get(self, request, format=None):
        data = {
            "Highlighter": reverse("highlighter:highlight", request=request, format=format),
            "Options": {
                "Languages": reverse("highlighter:highlight-options", request=request, format=format, args=['languages']),
                "Formats": reverse("highlighter:highlight-options", request=request, format=format, args=['formats']),
                "Styles": reverse("highlighter:highlight-options", request=request, format=format, args=['styles']),
            }
        }
        return Response(data, status=status.HTTP_200_OK)

