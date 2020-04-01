from django import forms

from crispy_forms.helper import FormHelper


class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = kwargs.pop("helper", FormHelper())


class TextInputForm(BaseForm):

    field_name = forms.CharField(
        label="Field label",
        widget=forms.TextInput(attrs={"width": "4"}),
        help_text="Help text",
        error_messages={"required": "Required error message"},
    )
