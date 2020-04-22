from django import forms
from django.utils.translation import ugettext_lazy as _

from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import Submit


class CheckboxForm(forms.Form):

    accept = forms.BooleanField(
        label=_("I accept the terms of service"),
        help_text=_(
            "Please read the terms of service and indicate whether you accept them."
        ),
        error_messages={"required": _("You must accept our terms of service")},
    )

    def __init__(self, *args, **kwargs):
        super(CheckboxForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit("submit", _("Submit")))
