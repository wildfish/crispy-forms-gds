from django import forms

from crispy_forms.helper import FormHelper


class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = kwargs.pop("helper", FormHelper())


class TextInputForm(BaseForm):

    name = forms.CharField(
        label="Name",
        widget=forms.TextInput,
        help_text="Help text",
        error_messages={"required": "Required error message"},
    )
