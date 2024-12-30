from django import forms

from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import HTML, Accordion, AccordionSection, Layout


class AccordionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Accordion(
                AccordionSection(
                    "Writing well for the web",
                    HTML.p("This is the content for Writing well for the web."),
                    summary="An introduction to clear and concise writing.",
                ),
                AccordionSection(
                    "Writing well for specialists",
                    HTML.p("This is the content for Writing well for specialists."),
                ),
                AccordionSection(
                    "Know your audience",
                    HTML.p("This is the content for Know your audience."),
                ),
                AccordionSection(
                    "How people read",
                    HTML.p("This is the content for How people read."),
                ),
            )
        )
