from django import forms

from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import Field, Layout, Size, Submit


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
            Field.radios("method", legend_size=Size.MEDIUM, small=True),
        )
        self.helper.add_input(Submit("submit", "Submit"))
