from pygments.formatters.terminal256 import Terminal256Formatter
from pygments.formatters.terminal import TerminalFormatter
from pygments.formatters.bbcode import BBCodeFormatter
from pygments.formatters.other import NullFormatter
from pygments.formatters.html import HtmlFormatter
from pygments.formatters.rtf import RtfFormatter
from pygments.formatters.svg import SvgFormatter
from pygments.formatters.irc import IRCFormatter
from pygments.lexers import get_lexer_by_name
from pygments.styles import get_style_by_name
from pygments.formatters.img import (
    GifImageFormatter, ImageFormatter,
    JpgImageFormatter, BmpImageFormatter,
)
from pygments import highlight
from pathlib import Path

# get required details
get_lexer: str = input('Language name: ')
get_code: str = input('Create simple snippet: ')
get_style: str = input('Styling name: ')
get_format: str = input('Format: ')

lexer = get_lexer_by_name(get_lexer, stripall=True)
style = get_style_by_name(get_style)

if get_format.lower() in ['bbcode', 'bb']:
    formatter = BBCodeFormatter(style=style, codetag=True, monofont=True)
    highlighted = highlight(code=get_code, lexer=lexer, formatter=formatter)
    result = Path('bbcoderesult')
    result.write_text(data=highlighted)

elif get_format.lower() in ['bmp', 'bitmap']:
    formatter = BmpImageFormatter(
        style=style, font_size=16, line_numbers=True, line_number_bg=None,
        image_format='bmp', line_number_bold=False, line_number_italic=False,
        line_number_separator=False, line_number_fg='#FFF',
    )
    highlight(code=get_code, lexer=lexer, formatter=formatter, outfile='result.bmp')

elif get_format.lower() in ['gif']:
    formatter = GifImageFormatter(
        style=style, font_size=16, line_numbers=True, line_number_bg=None,
        image_format='gif', line_number_bold=False, line_number_italic=False,
        line_number_separator=False, line_number_fg='#FFF',
    )
    print(highlight(code=get_code, lexer=lexer, formatter=formatter))

elif get_format.lower() in ['img', 'png', 'image']:
    formatter = ImageFormatter(
        style=style, font_size=16, line_numbers=True, line_number_bg=None,
        image_format='PNG', line_number_bold=False, line_number_italic=False,
        line_number_separator=True, line_number_fg='#FFF', 
    )
    highlight(code=get_code, lexer=lexer, formatter=formatter, outfile='result.png')

elif get_format.lower() in ['irc']:
    formatter = IRCFormatter(bg='dark', linenos=True)
    highlighted = highlight(code=get_code, lexer=lexer, formatter=formatter)
    result = Path('result.irc')
    result.write_text(data=highlighted)

elif get_format.lower() in ['jpg', 'jpeg']:
    formatter = JpgImageFormatter(
        style=style, font_size=16, line_numbers=True, line_number_bg=None,
        image_format='PNG', line_number_bold=False, line_number_italic=False,
        line_number_separator=True, line_number_fg='#FFF',
    )
    highlight(code=get_code, lexer=lexer, formatter=formatter, outfile='result.jpg')

elif get_format.lower() in ['rtf']:
    formatter = RtfFormatter(style=style, fontsize=28)
    highlighted = highlight(code=get_code, lexer=lexer, formatter=formatter)
    result = Path('result.rtf')
    result.write_text(data=highlighted)

elif get_format.lower() in ['txt', 'text', 'null']:
    formatter = NullFormatter()
    highlight(code=get_code, lexer=lexer, formatter=formatter, outfile='result.txt')

elif get_format.lower() in ['svg']:
    formatter = SvgFormatter(
        style=style, nowrap=False, fontfamily='monospace',
        fontsize='16px', linenos=False,
    )
    print(highlight(code=get_code, lexer=lexer, formatter=formatter))
    
elif get_format.lower() in ['html', 'htm']:
    formatter = HtmlFormatter(
        style=style, linenos='inline', noclasses=True, cssclass='pygment',
        wrapcode=True, nobackground=True,
    )
    highlighted = highlight(code=get_code, lexer=lexer, formatter=formatter)
    result = Path('result.html')
    result.write_text(data=highlighted)

elif get_format.lower() in ['terminal256', 'console256', '256']:
    formatter = Terminal256Formatter(style=style)
    highlighted = highlight(code=get_code, lexer=lexer, formatter=formatter)
    result = Path('terminal256')
    result.write_text(data=highlighted)

elif get_format.lower() in ['terminal', 'console']:
    formatter = TerminalFormatter(bg='dark', colorscheme=None, linenos=True)
    highlighted = highlight(code=get_code, lexer=lexer, formatter=formatter)
    result = Path('terminal')
    result.write_text(data=highlighted)