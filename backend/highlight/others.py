from rest_framework.renderers import JSONRenderer


class PrettyJSONRenderer(JSONRenderer):
    """
    Custom json renderer which subclasses the restframework JSONRenderer
    and edits the get_indent method to prettify the returned result by
    indenting it.
    """
    def get_indent(self, accepted_media_type, renderer_context):
        # this indents by 4
        return 4
