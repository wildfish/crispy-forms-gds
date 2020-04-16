from django import forms
from django.utils.translation import ugettext_lazy as _

from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import Field, Layout, Submit


class SelectForm(forms.Form):

    method = forms.ChoiceField(
        choices=(
            ("", _("Choose")),
            ("email", _("Email")),
            ("phone", _("Phone")),
            ("text", _("Text message")),
        ),
        widget=forms.Select,
        label=_("How would you like to be contacted?"),
        help_text=_("Select the most convenient way to contact you."),
        error_messages={"required": _("Enter the best way to contact you")},
    )

    def __init__(self, *args, **kwargs):
        super(SelectForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", _("Submit")))
