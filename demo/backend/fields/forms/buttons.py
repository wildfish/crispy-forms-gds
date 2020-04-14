from django import forms
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout

from crispy_forms_gds.layout import Button


class ButtonsForm(forms.Form):

    use_required_attribute = False

    name = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super(ButtonsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field("name", css_class="govuk-input"),
            Button(
                "primary",
                _("Primary button"),
                css_class="govuk-button",
                data_module="govuk-button",
            ),
            Button(
                "secondary",
                _("Secondary button"),
                css_class="govuk-button--secondary",
                data_module="govuk-button",
            ),
            Button(
                "disabled",
                _("Disabled button"),
                disabled="disabled",
                aria_disabled="true",
                data_module="govuk-button",
            ),
            Button(
                "warning",
                _("Warning button"),
                css_class="govuk-button--warning",
                data_module="govuk-button",
            ),
        )
