from django import forms

from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import Submit


class FileUploadForm(forms.Form):

    file = forms.FileField(
        label="Upload a file",
        help_text="Select the CSV file to upload.",
        error_messages={
            "required": "Choose the CSV file you exported from the spreadsheet"
        },
    )

    def __init__(self, *args, **kwargs):
        super(FileUploadForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit("submit", "Submit"))
