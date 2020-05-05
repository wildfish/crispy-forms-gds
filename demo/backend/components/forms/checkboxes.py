from django import forms
from django.forms import HiddenInput, MultipleHiddenInput

from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import HTML, Field, Layout, Size, Submit


class CheckboxesForm(forms.Form):

    method = forms.MultipleChoiceField(
        choices=(("email", "Email"), ("phone", "Phone"), ("text", "Text message"),),
        widget=forms.CheckboxSelectMultiple,
        label="How would you like to be contacted?",
        help_text="Select all options that are relevant to you.",
        error_messages={"required": "Enter the ways to contact you"},
    )

    accept = forms.BooleanField(
        label="I accept the terms of service",
        help_text="Please read the terms of service and indicate whether you accept them.",
        error_messages={"required": "You must accept our terms of service"},
    )

    def __init__(self, *args, **kwargs):
        super(CheckboxesForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field.checkboxes(
                "method",
                legend_size=Size.MEDIUM,
                small=True,
                hints={"phone": "Select this option only if you have a mobile phone"},
            ),
            Field.checkboxes("accept"),
            Submit("submit", "Submit"),
        )

    def get_method(self):
        value = self.cleaned_data["method"]
        choices = dict(self.fields["method"].choices)
        return ", ".join([choices.get(item) for item in value])

    def get_accept(self):
        value = self.cleaned_data["accept"]
        return "Yes" if value else "No"

    def valid_layout(self):
        self.fields["method"].widget = MultipleHiddenInput()
        self.fields["accept"].widget = HiddenInput()
        self.helper.layout = Layout(
            "method",
            "accept",
            HTML.h2("You answered..."),
            HTML.table(
                None,
                [
                    ("Methods selected:", self.get_method()),
                    ("Terms accepted:", self.get_accept()),
                ],
            ),
            Submit("continue", "Continue"),
        )
