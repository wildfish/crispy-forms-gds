from django import forms
from django.utils.translation import ugettext_lazy as _

from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import HTML, Layout


class WarningForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(WarningForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML.warning(
                _(
                    "You can be fined up to £5,000 if you do not like this template pack."
                )
            )
        )
