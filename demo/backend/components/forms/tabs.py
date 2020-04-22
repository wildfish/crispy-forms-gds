from django import forms
from django.utils.translation import ugettext_lazy as _

from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import HTML, Layout, Tabs, TabPanel


class TabsForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(TabsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Tabs(
                TabPanel(
                    _("First Tab"), HTML("<p>The first tab has these contents.</p>")
                ),
                TabPanel(
                    _("Second Tab"),
                    HTML(
                        "<p>However the contents are quite different in the second tab.</p>"
                    ),
                ),
            )
        )
