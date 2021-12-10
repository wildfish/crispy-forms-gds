from django import forms
from django.utils.translation import gettext_lazy as _

from crispy_forms_gds.fields import DateInputField
from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import HTML, Button, Hidden, Layout


class DateInputForm(forms.Form):

    date = DateInputField(
        label="When was your passport issued?",
        help_text="For example, 12 11 2007",
        require_all_fields=False,
    )

    def __init__(self, *args, **kwargs):
        super(DateInputForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout("date", Button("submit", _("Submit")))

        self.fields["date"].fields[2].error_messages[
            "incomplete"
        ] = "The date your passport was issued must include a year"

    def valid_layout(self):
        value = self.cleaned_data["date"]
        self.helper.layout = Layout(
            Hidden("date_0", value.day),
            Hidden("date_1", value.month),
            Hidden("date_2", value.year),
            HTML.h2("You answered..."),
            HTML.table(None, [("Date:", value.strftime("%e %B %Y"))]),
            Button("continue", "Continue"),
        )
