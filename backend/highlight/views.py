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
from pygments.lexers import get_lexer_by_name
from pygments.styles import get_style_by_name
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from pygments import highlight

# create class api
class Highlighter(APIView):
    """
    Class API view.

    post:
    only allows post request along side the data(code text) to highlight.
    """
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        code: str = request.data.get('code')
        lexer = get_lexer_by_name(request.data.get('lexer'), stripall=True)
        style = get_style_by_name(request.data.get('style'))
        get_format: str = request.data.get('format')

        #---more options, for formatters that require this settings.
        # linenos is used to request if the result should have line numbers
        # or not, this can be one of ['inline', 'table', False], defaults to
        # False, no line numbers
        linenos = request.data.get('linenos')
        
        # noclasses is used to define if the user requires inline css
        # styling or classes, if set to True inline styling is used and
        # the 'full, separate and other optional arguments will not take
        # effect, defaults to True
        noclasses: bool = request.data.get('noclasses')
        
        # class name to wrap the whole code block, defaults to highlighter,
        # NOTE: if linenos is set to table the cssclass name will append a 
        # 'table' making it 'highlightertable'.
        cssclass: str = request.data.get('cssclass')

        # Specify a list of lines to be highlighted in your result.
        hl_lines: list = request.data.get('hl_lines')
        
        # should the style selected also affect the overall code background?
        # defaults to False
        nobackground: bool = request.data.get('nobackground')
        
        # full is used to define if the user requires a full html
        # document, defaults to False
        full: bool = request.data.get('full')
        
        # the title of the html document if full is set to True
        title: str = request.data.get('title')

        # separate is used along side 'full' argument to request a separate
        # css style result and a body result, default to False
        separate: bool = request.data.get('seperate')
        
        # prefix the css classes used when 'noclasses' is set to False
        classprefix: str = request.data.get('classprefix')

        # which formatter was selected by the user?
        if get_format.lower() in ['bbcode', 'bb']:
            formatter = BBCodeFormatter(style=style, codetag=True, monofont=True)
            highlighted = highlight(code, lexer, formatter)
            data = {"status": "success", "result": highlighted}
            return Response(data=data, status=status.HTTP_200_OK)

        elif get_format.lower() in ['irc']:
            formatter = IRCFormatter(bg='dark', linenos=linenos)
            highlighted = highlight(code, lexer, formatter)
            data = {"status": "success", "result": highlighted}
            return Response(data=data, status=status.HTTP_200_OK)

        elif get_format.lower() in ['rtf']:
            formatter = RtfFormatter(style=style, fontsize=28)
            highlighted = highlight(code, lexer, formatter)
            data = {"status": "success", "result": highlighted}
            return Response(data=data, status=status.HTTP_200_OK)

        elif get_format.lower() in ['txt', 'text', 'null']:
            formatter = NullFormatter()
            highlighted = highlight(code, lexer, formatter)
            data = {"status": "success", "result": highlighted}
            return Response(data=data, status=status.HTTP_200_OK)

        elif get_format.lower() in ['svg']:
            formatter = SvgFormatter(
                style=style, nowrap=False, fontfamily='monospace',
                fontsize='16px', linenos=linenos,
            )
            highlighted = highlight(code, lexer, formatter)
            data = {"status": "success", "result": highlighted}
            return Response(data=data, status=status.HTTP_200_OK)

        elif get_format.lower() in ['html', 'htm']:
            formatter = HtmlFormatter(
                style=style, linenos=linenos, noclasses=noclasses,
                wrapcode=True, nobackground=nobackground, cssclass=cssclass,
                hl_lines=hl_lines,
            )
            highlighted = highlight(code, lexer, formatter)
            data = {"status": "success", "result": highlighted}
            return Response(data=data, status=status.HTTP_200_OK)

        # the terminal formatters should only be used while in terminal interfaces
        elif get_format.lower() in ['terminal256', 'console256', '256']:
            formatter = Terminal256Formatter(style=style)
            highlighted = highlight(code, lexer, formatter)
            data = {"status": "success", "result": highlighted}
            return Response(data=data, status=status.HTTP_200_OK)

        elif get_format.lower() in ['terminal', 'console']:
            formatter = TerminalFormatter(bg='dark', colorscheme=None, linenos=linenos)
            highlighted = highlight(code, lexer, formatter)
            data = {"status": "success", "result": highlighted}
            return Response(data=data, status=status.HTTP_200_OK)