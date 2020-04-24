from django import forms

from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import HTML, Layout


class InsetForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(InsetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML.inset(
                "It can take up to 8 weeks to register a lasting power of "
                "attorney if there are no mistakes in the application. "
            )
        )
