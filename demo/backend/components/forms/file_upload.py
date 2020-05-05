from django import forms
from django.urls import reverse

from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import HTML, Layout, Submit


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
        self.helper = FormHelper()
        self.helper.layout = Layout("file", Submit("submit", "Submit"))

    def valid_layout(self):
        file = self.cleaned_data["file"]
        self.helper.layout = Layout(
            HTML.h2("You uploaded..."),
            HTML.p("File: %s" % file),
            HTML(
                '<a class="govuk-button" href="%s">Continue</a>'
                % reverse("components:name", kwargs={"name": "file-upload"})
            ),
        )
