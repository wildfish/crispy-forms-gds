from django import forms
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout

from crispy_forms_gds.layout import Submit


class FileUploadForm(forms.Form):

    use_required_attribute = False

    file = forms.FileField(
        label=_("Upload a file"),
        help_text=_("Select the CSV file to upload."),
        error_messages={
            "required": _("Select the CSV file you exported from the spreadsheet")
        },
    )

    def __init__(self, *args, **kwargs):
        super(FileUploadForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field("file", css_class="govuk-file-upload",), Submit("submit", "Submit"),
        )
