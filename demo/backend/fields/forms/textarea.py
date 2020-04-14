from django import forms
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout

from crispy_forms_gds.layout import Submit


class TextareaForm(forms.Form):

    use_required_attribute = False

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
            Field(
                "description",
                css_class="govuk-textarea",
                autocomplete="off",
                spellcheck="true",
                rows=3,
            ),
            Submit("submit", _("Submit")),
        )
