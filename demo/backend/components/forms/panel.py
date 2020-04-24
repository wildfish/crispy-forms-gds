from django import forms

from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import HTML, Layout


class PanelForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(PanelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML.panel(
                "Application complete",
                "Your reference number <strong>HDJ2123F</strong>",
            )
        )
