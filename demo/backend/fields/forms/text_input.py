from django import forms
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout

from crispy_forms_gds.layout import Submit


class TextInputForm(forms.Form):

    use_required_attribute = False

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

    age = forms.IntegerField(
        label=_("Age"),
        help_text=_("How old are you?"),
        widget=forms.TextInput,
        error_messages={"required": _("Enter how old you were on your last birthday")},
    )

    def __init__(self, *args, **kwargs):
        super(TextInputForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field(
                "name",
                css_class="govuk-input",
                autocomplete="name",
                spellcheck="false",
            ),
            Field(
                "email",
                type="email",
                css_class="govuk-input govuk-!-width-one-half",
                autocomplete="email",
                spellcheck="false",
            ),
            Field(
                "age",
                css_class="govuk-input govuk-input--width-3",
                pattern="[0-9]*",
                inputmode="numeric",
            ),
            Submit("submit", _("Submit")),
        )
