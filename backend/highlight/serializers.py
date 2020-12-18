from rest_framework import serializers
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

#--initialize variables
# get all lexers in list format
LEXERS = [lexer for lexer in get_all_lexers()]
# organize all lexers in tuples with two values ('lexer', 'LEXER')
LANGUAGES = sorted([(lexer[0].lower(), lexer[1][0]) for lexer in LEXERS])
# get and organize all styles available for highlighting the code snippet.
STYLES = sorted([(style, style) for style in get_all_styles()])
# available formatters as @ version 0.1.1 (not released).
# hardcoded.
FORMATTERS = sorted((
    ('bbcode', 'bbcode'),
    ('html', 'html'),
    ('irc', 'irc'),
    ('rtf', 'rtf'),
    ('svg', 'svg'),
    ('text', 'text'),
    ('terminal', 'terminal'),
    ('terminal256', 'terminal256'),
))
# a tuple of the line number formats available.
LINENUMBER = (
    ('none', 'none'),
    ('table', 'table'),
    ('inline', 'inline'),
)
# HTML: the css styling formats available. inline or class.
CSS = (
    ('inline', 'inline'),
    ('class', 'class')
)


class HighlighterSerializer(serializers.Serializer):
    """
    Serializer for the api post request.
    """
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    language = serializers.ChoiceField(choices=LANGUAGES, default='python')
    style = serializers.ChoiceField(choices=STYLES, default='emacs')
    getFormat = serializers.ChoiceField(choices=FORMATTERS, default='html')
    lineNos = serializers.ChoiceField(choices=LINENUMBER, required=False, default='none')
    css = serializers.ChoiceField(choices=CSS, required=False, default='inline')
    divClass = serializers.CharField(required=False, default='justhighlight')
    hlLines = serializers.ListField(
        required=False,
        default=[],
        # child=serializers.IntegerField(min_value=1) #validator
    )
    noBackground = serializers.BooleanField(required=False, default=False)
    classPrefix = serializers.CharField(required=False, max_length=10, default='')
    # full = serializers.BooleanField(required=False, default=False)
    # title = serializers.CharField(required=False)
    # separate = serializers.BooleanField(required=False, default=False)

    # This serializer does not create nor updates any model instance.
