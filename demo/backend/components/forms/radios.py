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

    def __init__(self, *args, **kwargs):
        super(RadiosForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field.radios("name", legend_size=Size.MEDIUM, legend_tag="h1")
        )
        self.helper.add_input(Submit("submit", "Submit"))
