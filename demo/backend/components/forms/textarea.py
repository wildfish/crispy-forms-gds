from django import forms

from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import HTML, Button, Field, Hidden, Layout


class TextareaForm(forms.Form):

    description = forms.CharField(
        label="Can you provide more detail?",
        widget=forms.Textarea,
        help_text="Do not include personal or financial information, like your "
        "National Insurance number or credit card details.",
        error_messages={"required": "Enter a short description of your application"},
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field.textarea("description", rows=3, max_words=100,),
            Button("submit", "Submit"),
        )

    def valid_layout(self):
        value = self.cleaned_data["description"]
        self.helper.layout = Layout(
            Hidden("description", value),
            HTML.h2("You answered..."),
            HTML.p(value),
            Button("continue", "Continue"),
        )
