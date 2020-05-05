from django import forms

from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import HTML, Field, Hidden, Layout, Size, Submit


class RadiosForm(forms.Form):

    name = forms.ChoiceField(
        choices=(("yes", "Yes"), ("no", "No")),
        widget=forms.RadioSelect,
        label="Have you changed your name?",
        help_text="This includes changing your last name or spelling your name differently.",
        error_messages={"required": "Enter whether your name has changed"},
    )

    method = forms.ChoiceField(
        choices=(("email", "Email"), ("phone", "Phone"), ("text", "Text message"),),
        widget=forms.RadioSelect,
        label="How would you like to be contacted?",
        help_text="Select the options that is best for you.",
        error_messages={
            "required": "Select the best way to send a confirmation message"
        },
    )

    def __init__(self, *args, **kwargs):
        super(RadiosForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field.radios("name", legend_size=Size.MEDIUM, legend_tag="h1", inline=True),
            Field.radios(
                "method",
                legend_size=Size.MEDIUM,
                small=True,
                hints={"phone": "Select this option only if you have a mobile phone"},
            ),
            Submit("submit", "Submit"),
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
            Submit("continue", "Continue"),
        )
