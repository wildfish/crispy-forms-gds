from django import forms

from crispy_forms_gds.fields import DateInputField
from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import (
    HTML,
    Accordion,
    AccordionSection,
    Fieldset,
    Layout,
    TabPanel,
    Tabs,
)


class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)


class CheckboxForm(BaseForm):

    accept = forms.BooleanField(
        label="I accept the terms of service",
        help_text="Please read the terms of service.",
        error_messages={"required": "You must accept our terms of service"},
    )


class CheckboxesForm(BaseForm):

    method = forms.ChoiceField(
        choices=(("email", "Email"), ("phone", "Phone"), ("text", "Text message")),
        widget=forms.CheckboxSelectMultiple,
        label="How would you like to be contacted?",
        help_text="Select all options that are relevant to you.",
        error_messages={"required": "Enter the ways to contact you"},
    )


class DateInputForm(BaseForm):

    date = DateInputField(
        label="When was your passport issued?",
        help_text="For example, 12 11 2007",
        require_all_fields=False,
    )


class FileUploadForm(BaseForm):

    file = forms.FileField(
        label="Upload a file",
        help_text="Select the CSV file to upload.",
        error_messages={
            "required": "Select the CSV file you exported from the spreadsheet"
        },
    )


class RadiosForm(BaseForm):

    method = forms.ChoiceField(
        choices=(("email", "Email"), ("phone", "Phone"), ("text", "Text message")),
        widget=forms.RadioSelect,
        label="How would you like to be contacted?",
        help_text="Select the most convenient way to contact you.",
        error_messages={"required": "Enter the best way to contact you"},
    )


class SelectForm(BaseForm):

    method = forms.ChoiceField(
        choices=(
            ("", "Choose"),
            ("email", "Email"),
            ("phone", "Phone"),
            ("text", "Text message"),
        ),
        widget=forms.Select,
        label="How would you like to be contacted?",
        help_text="Select the most convenient way to contact you.",
        error_messages={"required": "Enter the best way to contact you"},
    )


class TextInputForm(BaseForm):

    name = forms.CharField(
        label="Name",
        help_text="Help text",
        error_messages={"required": "Required error message"},
    )


class TextareaForm(BaseForm):

    description = forms.CharField(
        label="Description",
        widget=forms.Textarea,
        help_text="Help text",
        error_messages={"required": "Required error message"},
    )


class TableForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        header = ["Case worker", "Number of cases closed"]
        rows = [["David Francis", 3], ["Paul Farmer", 1]]
        header_css = [
            "govuk-!-width-one-half",
            "govuk-!-width-one-half govuk-table__header--numeric",
        ]
        row_css = ["", "govuk-table__cell--numeric"]

        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML.table(
                header, rows, caption="Caption", header_css=header_css, row_css=row_css
            )
        )


class TabsForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Tabs(
                TabPanel("First Tab", HTML("<p>First panel</p>")),
                TabPanel("Second Tab", HTML("<p>Second panel</p>")),
            )
        )


class FieldsetForm(forms.Form):

    name = forms.CharField(label="Name")
    email = forms.CharField(label="Email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(Fieldset("name", "email", legend="Contact"))


class AccordionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Accordion(
                AccordionSection(
                    "First section",
                    HTML("<p>First section contents.</p>"),
                    summary="A summary of the first section",
                ),
                AccordionSection(
                    "Second section", HTML("<p>Second section contents.</p>"),
                ),
            )
        )
