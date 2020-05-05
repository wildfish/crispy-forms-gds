from django import forms

from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import (
    HTML,
    Field,
    Fieldset,
    Fixed,
    Fluid,
    Hidden,
    Layout,
    Size,
    Submit,
)


class TextInputForm(forms.Form):

    name = forms.CharField(
        label="Your name", help_text="Enter your name as it appears on your passport.",
    )

    email = forms.CharField(label="Email", help_text="Enter your email address.",)

    phone = forms.CharField(
        label="Phone", help_text="Enter your home or mobile telephone number.",
    )

    def __init__(self, *args, **kwargs):
        super(TextInputForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.label_size = Size.SMALL
        self.helper.layout = Layout(
            Fieldset(
                Field.text("name"),
                Field.text("email", field_width=Fluid.TWO_THIRDS),
                Field.text("phone", field_width=Fixed.TEN),
            ),
            Submit("submit", "Submit"),
        )

    def valid_layout(self):
        name = self.cleaned_data["name"]
        email = self.cleaned_data["email"]
        phone = self.cleaned_data["phone"]
        self.helper.layout = Layout(
            Hidden("name", name),
            Hidden("email", email),
            Hidden("phone", phone),
            HTML.h2("You answered..."),
            HTML.table(None, [("Name:", name), ("Email:", email), ("Phone:", phone)]),
            Submit("continue", "Continue"),
        )
