from django import forms
from django.utils.translation import ugettext_lazy as _

from crispy_forms_gds.fields import DateInputField
from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import Submit


class DateInputForm(forms.Form):

    date = DateInputField(
        label="When was your passport issued?",
        help_text="For example, 12 11 2007",
        require_all_fields=False,
    )

    def __init__(self, *args, **kwargs):
        super(DateInputForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit("submit", _("Submit")))

        self.fields["date"].fields[2].error_messages[
            "incomplete"
        ] = "The date your passport was issued must include a year"
