from django import forms

from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import (
    HTML,
    Button,
    ConditionalQuestion,
    ConditionalRadios,
    Hidden,
    Layout,
)


class ConditionalRadiosForm(forms.Form):
    method = forms.ChoiceField(
        choices=(
            ("phone", "By phone"),
            ("email", "By email"),
            ("no_contact", "Do not contact me"),
        ),
    )
    mobile_phone_number = forms.CharField(required=False)
    home_phone_number = forms.CharField(required=False)
    email_address = forms.EmailField(required=False, max_length="320")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            ConditionalRadios(
                "method",
                ConditionalQuestion(
                    "By phone",
                    "mobile_phone_number",
                    "home_phone_number",
                    HTML.p("Please enter either mobile or home"),
                ),
                ConditionalQuestion(
                    "By email",
                    "email_address",
                ),
                "Do not contact me",
            ),
            Button("submit", "Submit"),
        )

    def clean(self):
        method = self.cleaned_data["method"]
        mobile_phone_number = self.cleaned_data["mobile_phone_number"]
        home_phone_number = self.cleaned_data["home_phone_number"]
        email_address = self.cleaned_data["email_address"]

        if method == "phone":
            if not mobile_phone_number and not home_phone_number:
                self.add_error(
                    "mobile_phone_number",
                    "Please enter your mobile or home phone number",
                )
        elif method == "email":
            if not email_address:
                self.add_error("email_address", "Please enter an email address")

        return self.cleaned_data

    def valid_layout(self):
        method = self.cleaned_data["method"]
        mobile_phone_number = self.cleaned_data["mobile_phone_number"]
        home_phone_number = self.cleaned_data["home_phone_number"]
        email_address = self.cleaned_data["email_address"]

        if method == "phone":
            label = "Mobile phone"
            if mobile_phone_number:
                label = "Mobile"
                contact = mobile_phone_number
            else:
                label = "Home phone"
                contact = home_phone_number
        elif method == "email":
            label = "Email"
            contact = email_address
        else:
            label = None
            contact = None

        if label:
            response = Layout(
                HTML.h2("You wish to be contacted by..."),
                HTML.table(None, [(label, contact)]),
            )
        else:
            response = HTML.h2("You do not wish to be contacted")

        self.helper.layout = Layout(
            Hidden("method", method),
            Hidden("mobile_phone_number", mobile_phone_number),
            Hidden("home_phone_number", home_phone_number),
            Hidden("email_address", email_address),
            response,
            Button("continue", "Continue"),
        )
