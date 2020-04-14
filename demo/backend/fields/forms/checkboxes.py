from django import forms
from django.forms import CheckboxSelectMultiple
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms_gds.layout import Submit


class CheckboxesForm(forms.Form):

    use_required_attribute = False

    method = forms.ChoiceField(
        choices=(
            ("email", _("Email")),
            ("phone", _("Phone")),
            ("text", _("Text message")),
        ),
        widget=CheckboxSelectMultiple,
        label=_("How would you like to be contacted?"),
        help_text=_("Select all options that are relevant to you."),
        error_messages={"required": _("Enter the ways to contact you")},
    )

    def __init__(self, *args, **kwargs):
        super(CheckboxesForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", _("Submit")))
