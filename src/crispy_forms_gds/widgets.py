from django import forms
from django.utils.translation import ugettext_lazy as _


class DateInputWidget(forms.MultiWidget):
    template_name = "gds/widgets/date.html"

    def __init__(self, *args, **kwargs):
        widgets = [
            forms.TextInput(
                attrs={
                    "class": "govuk-input govuk-date-input__input govuk-input--width-2",
                    "label": _("Day"),
                }
            ),
            forms.TextInput(
                attrs={
                    "class": "govuk-input govuk-date-input__input govuk-input--width-2",
                    "label": _("Month"),
                }
            ),
            forms.TextInput(
                attrs={
                    "class": "govuk-input govuk-date-input__input govuk-input--width-4",
                    "label": _("Year"),
                }
            ),
        ]
        super(DateInputWidget, self).__init__(widgets, **kwargs)

    def decompress(self, value):
        if value:
            return value.day, value.month, value.year
        return None, None, None
