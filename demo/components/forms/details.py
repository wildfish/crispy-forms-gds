from django import forms

from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import HTML, Layout


class DetailsForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML.details(
                "Help with nationality",
                "We need to know your nationality so we can work out which "
                "elections you’re entitled to vote in. If you cannot provide "
                "your nationality, you’ll have to send copies of identity "
                "documents through the post.",
            )
        )
