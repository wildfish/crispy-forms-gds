from django import forms
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms_gds.layout import Submit


class TextInputForm(forms.Form):

    name = forms.CharField(
        label=_("Name"),
        widget=forms.TextInput(),
        help_text=_("Your full name."),
        error_messages={
            "required": _("Enter your name as it appears on your passport")
        }
    )

    age = forms.CharField(
        label=_("Age"),
        widget=forms.TextInput(attrs={"width": 4}),
        help_text=_("How old are you?"),
        error_messages={
            "required": _("Enter your age on your last birthday")
        }
    )

    def __init__(self, *args, **kwargs):
        super(TextInputForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", _("Submit")))
