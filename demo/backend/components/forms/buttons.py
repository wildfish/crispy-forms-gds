from django import forms

from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import Button, Div, Layout, Submit


class ButtonsForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ButtonsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(Button.primary("continue", "Save and continue")),
            Div(Button.secondary("find", "Find address")),
            Div(Button.secondary("win", "Win lottery", disabled=True)),
            Div(Button.warning("delete", "Delete account")),
            Div(Submit("submit", "Submit")),
        )
