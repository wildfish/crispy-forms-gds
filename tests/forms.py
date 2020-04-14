from django import forms
from django.forms import CheckboxSelectMultiple, RadioSelect, Select, Textarea

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

from crispy_forms_gds.layout import Button


class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = kwargs.pop("helper", FormHelper())


class ButtonsForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ButtonsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Button("primary", "Primary button", data_module="govuk-button"),
            Button(
                "secondary",
                "Secondary button",
                css_class="govuk-button--secondary",
                data_module="govuk-button",
            ),
            Button(
                "disabled",
                "Disabled button",
                disabled="disabled",
                aria_disabled="true",
                data_module="govuk-button",
            ),
            Button(
                "warning",
                "Warning button",
                css_class="govuk-button--warning",
                data_module="govuk-button",
            ),
        )


class TextInputForm(BaseForm):

    use_required_attribute = False

    name = forms.CharField(
        label="Name",
        help_text="Help text",
        error_messages={"required": "Required error message"},
    )


class TextareaForm(BaseForm):

    use_required_attribute = False

    name = forms.CharField(
        label="Name",
        widget=Textarea,
        help_text="Help text",
        error_messages={"required": "Required error message"},
    )


class CheckboxesForm(forms.Form):

    use_required_attribute = False

    method = forms.ChoiceField(
        choices=(("email", "Email"), ("phone", "Phone"), ("text", "Text message")),
        widget=CheckboxSelectMultiple,
        label="How would you like to be contacted?",
        help_text="Select all options that are relevant to you.",
        error_messages={"required": "Enter the ways to contact you"},
    )

    def __init__(self, *args, **kwargs):
        super(CheckboxesForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Submit"))


class FileUploadForm(forms.Form):

    use_required_attribute = False

    file = forms.FileField(
        label="Upload a file",
        help_text="Select the CSV file to upload.",
        error_messages={
            "required": "Select the CSV file you exported from the spreadsheet"
        },
    )


class RadiosForm(forms.Form):

    use_required_attribute = False

    method = forms.ChoiceField(
        choices=(("email", "Email"), ("phone", "Phone"), ("text", "Text message")),
        widget=RadioSelect,
        label="How would you like to be contacted?",
        help_text="Select the most convenient way to contact you.",
        error_messages={"required": "Enter the best way to contact you"},
    )

    def __init__(self, *args, **kwargs):
        super(RadiosForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Submit"))


class SelectForm(forms.Form):

    use_required_attribute = False

    method = forms.ChoiceField(
        choices=(
            ("", "Choose"),
            ("email", "Email"),
            ("phone", "Phone"),
            ("text", "Text message"),
        ),
        widget=Select,
        label="How would you like to be contacted?",
        help_text="Select the most convenient way to contact you.",
        error_messages={"required": "Enter the best way to contact you"},
    )

    def __init__(self, *args, **kwargs):
        super(SelectForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Submit"))
