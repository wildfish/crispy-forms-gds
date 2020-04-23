from django import forms
from django.utils.translation import ugettext_lazy as _

from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import HTML, Layout, Accordion, AccordionSection


class AccordionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(AccordionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Accordion(
                AccordionSection(
                    _("First section"),
                    HTML("<p>The first section has these contents.</p>"),
                ),
                AccordionSection(
                    _("Second section"),
                    HTML(
                        "<p>However the contents are quite different in the second section.</p>"
                    ),
                ),
                css_id="accordion",
            )
        )
