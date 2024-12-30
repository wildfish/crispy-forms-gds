from django import forms

from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import (
    HTML,
    Button,
    Field,
    Fieldset,
    Fixed,
    Fluid,
    Hidden,
    Layout,
    Size,
)


class TextInputForm(forms.Form):
    name = forms.CharField(
        label="Your name",
        help_text="Enter your name as it appears on your passport.",
    )

    email = forms.CharField(
        label="Email",
        help_text="Enter your email address.",
        widget=forms.EmailInput,
    )

    phone = forms.CharField(
        label="Phone",
        help_text="Enter your home or mobile telephone number.",
    )

    password = forms.CharField(
        label="Password",
        help_text="Enter your password.",
        widget=forms.PasswordInput,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.label_size = Size.SMALL
        self.helper.layout = Layout(
            Fieldset(
                Field.text("name"),
                Field.text("email", field_width=Fluid.TWO_THIRDS),
                Field.text("phone", field_width=Fixed.TEN),
                Field.text("password", field_width=Fluid.ONE_HALF),
            ),
            Button("submit", "Submit"),
        )

    def valid_layout(self):
        name = self.cleaned_data["name"]
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password"]
        phone = self.cleaned_data["phone"]
        self.helper.layout = Layout(
            Hidden("name", name),
            Hidden("email", email),
            Hidden("password", password),
            Hidden("phone", phone),
            HTML.h2("You answered..."),
            HTML.table(
                None,
                [
                    ("Name:", name),
                    ("Email:", email),
                    ("Phone:", phone),
                    ("Password:", password),
                ],
            ),
            Button("continue", "Continue"),
        )
