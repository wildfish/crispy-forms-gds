from django import forms
from django.utils.translation import ugettext_lazy as _

from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import HTML, Layout


class InsetForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(InsetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(HTML.inset(_("This is the inset text.")))
