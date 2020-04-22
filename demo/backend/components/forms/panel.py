from django import forms
from django.utils.translation import ugettext_lazy as _

from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import HTML, Layout


class PanelForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(PanelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML.panel(_("This is the title"), _("These are the contents."))
        )
