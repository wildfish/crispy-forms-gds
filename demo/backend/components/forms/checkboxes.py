from django import forms
from django.forms import MultipleHiddenInput

from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import HTML, Button, Field, Layout, Size


class CheckboxesForm(forms.Form):

    method = forms.MultipleChoiceField(
        choices=(("email", "Email"), ("phone", "Phone"), ("text", "Text message"),),
        widget=forms.CheckboxSelectMultiple,
        label="How would you like to be contacted?",
        help_text="Select all options that are relevant to you.",
        error_messages={"required": "Enter the ways to contact you"},
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field.checkboxes(
                "method",
                legend_size=Size.MEDIUM,
                small=True,
                hints={"phone": "Select this option only if you have a mobile phone"},
            ),
            Button("submit", "Submit"),
        )

    def get_method(self):
        value = self.cleaned_data["method"]
        choices = dict(self.fields["method"].choices)
        return ", ".join([choices.get(item) for item in value])

    def valid_layout(self):
        self.fields["method"].widget = MultipleHiddenInput()
        self.helper.layout = Layout(
            "method",
            HTML.h2("You answered..."),
            HTML.table(None, [("Methods selected:", self.get_method())]),
            Button("continue", "Continue"),
        )
