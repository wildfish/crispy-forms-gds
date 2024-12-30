from django import forms

from crispy_forms_gds.choices import Choice
from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import HTML, Button, Field, Hidden, Layout, Size


class RadiosForm(forms.Form):
    name = forms.ChoiceField(
        choices=(("yes", "Yes"), ("no", "No")),
        widget=forms.RadioSelect,
        label="Have you changed your name?",
        help_text="This includes changing your last name or spelling your name differently.",
        error_messages={"required": "Enter whether your name has changed"},
    )

    METHODS = (
        Choice("email", "Email", hint="Do not use an email address from work"),
        Choice("phone", "Phone", divider="Or"),
        Choice("text", "Text message"),
    )

    method = forms.ChoiceField(
        choices=METHODS,
        widget=forms.RadioSelect,
        label="How would you like to be contacted?",
        help_text="Select the options that is best for you.",
        error_messages={
            "required": "Select the best way to send a confirmation message"
        },
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field.radios("name", legend_size=Size.MEDIUM, legend_tag="h1", inline=True),
            Field.radios("method", legend_size=Size.MEDIUM, small=True),
            Button("submit", "Submit"),
        )

    def get_choice(self, field):
        value = self.cleaned_data[field]
        return dict(self.fields[field].choices).get(value)

    def valid_layout(self):
        name = self.cleaned_data["name"]
        method = self.cleaned_data["method"]
        self.helper.layout = Layout(
            Hidden("name", name),
            Hidden("method", method),
            HTML.h2("You answered..."),
            HTML.table(
                None,
                [
                    ("Name changed:", self.get_choice("name")),
                    ("Contact method:", self.get_choice("method")),
                ],
            ),
            Button("continue", "Continue"),
        )
