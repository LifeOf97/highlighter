from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from pygments import highlight, formatters
from pygments.lexers import get_lexer_by_name
from pygments.styles import get_style_by_name
from pygments.formatters import get_all_formatters, get_formatter_by_name

# get required details
get_lexer: str = input('Language name: ')
get_code: str = input('Create simple snippet: ')
get_style: str = input('Styling name: ')
get_format: str = input('Format: ')

lexer = get_lexer_by_name(get_lexer, stripall=True)
style = get_style_by_name(get_style)
formatter = get_formatter_by_name(get_format)

if 'html' in formatter.aliases:
    formatter(
        style=get_style, linenos='inline', noclasses=True, cssclass='pygment',
        wrapcode=True, nobackground=True,
    )
    highlight(code=get_code, lexer=get_lexer, formatter=formatter, outfile='result.html')

elif get_format in formatter.aliases:
    formatter(style=get_style, codetag=True, monofont=True)
    highlight(code=get_code, lexer=get_lexer, formatter=formatter, outfile='result.bb')

# highlight the code
