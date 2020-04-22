from django import forms
from django.utils.translation import ugettext_lazy as _

from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import Button, Layout


class ButtonsForm(forms.Form):

    name = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(ButtonsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "name",
            Button.primary("primary", _("Primary button")),
            Button.secondary("secondary", _("Secondary button")),
            Button.secondary("disabled", _("Disabled button"), disabled=True),
            Button.warning("warning", _("Warning button")),
        )
