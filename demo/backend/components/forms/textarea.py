from django import forms
from django.utils.translation import ugettext_lazy as _

from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import Field, Layout, Submit


class TextareaForm(forms.Form):

    description = forms.CharField(
        label=_("Can you provide more detail?"),
        widget=forms.Textarea,
        help_text=_(
            "Do not include personal or financial information, like your "
            "National Insurance number or credit card details."
        ),
        error_messages={"required": _("Enter a short description of your application")},
    )

    def __init__(self, *args, **kwargs):
        super(TextareaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field("description", autocomplete="off", spellcheck="true", rows=3,),
            Submit("submit", _("Submit")),
        )
