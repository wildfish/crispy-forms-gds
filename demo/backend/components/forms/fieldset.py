from django import forms
from django.utils.translation import ugettext_lazy as _

from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import Fieldset, Layout


class FieldsetForm(forms.Form):

    name = forms.CharField(
        label=_("Name"),
        help_text=_("Your full name."),
        error_messages={
            "required": _("Enter your name as it appears on your passport")
        },
    )

    email = forms.CharField(
        label=_("Email"),
        help_text=_("Your primary email address."),
        error_messages={
            "required": _("Enter an email address where we can contact you")
        },
    )

    def __init__(self, *args, **kwargs):
        super(FieldsetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset("name", "email", title="Contact", size="l", tag="h1")
        )
