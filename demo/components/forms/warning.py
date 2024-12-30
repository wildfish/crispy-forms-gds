from django import forms

from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import HTML, Layout


class WarningForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML.warning(
                "You can be fined up to £5,000 if you do not like this template pack."
            )
        )
