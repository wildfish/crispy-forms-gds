from django import forms
from django.utils.translation import gettext_lazy as _


class DateInputWidget(forms.MultiWidget):
    """
    A DateInputWidget defines the styling of the set of fields for displaying
    the value for a DateInputField.

    A custom widget was needed for two reasons. First the CSS classes needed to
    style the fields and set their width reduces the code need to add a Date input
    component to a form. Second, the Design System requires labels for the individual
    fields. That's not supported out of the box by a MultiValueField so the labels
    are added as a custom attribute and rendered with the correct markup in the
    template. The template also pops the label from the widget so it does not also
    get added as an attribute.

    """

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
        super().__init__(widgets, **kwargs)

    def decompress(self, value):
        """
        Convert a ``date`` into values for the day, month and year so it can be
        displayed in the widget's fields.

        Args:
            value (date): the date to be displayed

        Returns:
            a 3-tuple containing the day, month and year components of the date.

        """
        if value:
            return value.day, value.month, value.year
        return None, None, None
