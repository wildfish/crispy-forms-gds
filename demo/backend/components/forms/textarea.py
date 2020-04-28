from django import forms

from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import Field, Layout, Size, Submit


class TextareaForm(forms.Form):

    description = forms.CharField(
        label="Can you provide more detail?",
        widget=forms.Textarea,
        help_text="Do not include personal or financial information, like your "
        "National Insurance number or credit card details.",
        error_messages={
            "required": "Enter a short description of the problem you had "
            "making your purchase"
        },
    )

    def __init__(self, *args, **kwargs):
        super(TextareaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field.textarea(
                "description",
                label_size=Size.LARGE,
                label_tag="h1",
                rows=3,
                max_words=100,
            ),
            Submit("submit", "Submit"),
        )
