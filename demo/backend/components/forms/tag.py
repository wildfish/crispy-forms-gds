from django import forms
from django.utils.safestring import mark_safe

from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import HTML, Colour, Layout


class TagForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        headings = ["Name of user", "status"]
        statuses = [
            ["Rachel Silver", mark_safe(HTML.tag("Pending", Colour.BLUE).html)],
            ["Jesse Smith", mark_safe(HTML.tag("Inactive", Colour.PURPLE).html)],
            ["Joshua Wessel ", mark_safe(HTML.tag("Active", Colour.GREEN).html)],
            ["Tim Harvey", mark_safe(HTML.tag("Blocked", Colour.RED).html)],
            ["Rachael Pepper", mark_safe(HTML.tag("Disabled", Colour.GREY).html)],
            ["Stuart Say", mark_safe(HTML.tag("Declined", Colour.ORANGE).html)],
            ["Laura Frith", mark_safe(HTML.tag("Waiting", Colour.PINK).html)],
            ["Emma Tennant", mark_safe(HTML.tag("New", Colour.TURQUOISE).html)],
            ["Nigel Starmer", mark_safe(HTML.tag("Delayed", Colour.YELLOW).html)],
        ]

        self.helper = FormHelper()
        self.helper.layout = Layout(HTML.table(headings, statuses))
