from crispy_forms.layout import Submit
from django import forms

from crispy_forms.helper import FormHelper
from django.forms import CheckboxSelectMultiple, Textarea


class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = kwargs.pop("helper", FormHelper())


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
