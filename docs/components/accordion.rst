.. _Accordion: https://design-system.service.gov.uk/components/accordion/

#########
Accordion
#########
There are two Layout classes for adding an `Accordion`_ to a form. ``AccordionSection``
which wraps the contents of each section and ``Accordion`` which wraps the sections
and adds the ability to open and collapse them. ::

    from django import forms

    from crispy_forms_gds.helper import FormHelper
    from crispy_forms_gds.layout import Accordion, AccordionSection


    class AccordionForm(forms.Form):

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(
                Accordion(
                    AccordionSection(
                        "Writing well for the web",
                        HTML.p("This is the content for Writing well for the web.")
                    ),
                    AccordionSection(
                        "Writing well for specialists",
                        HTML.p("This is the content for Writing well for specialists.")
                    ),
                    AccordionSection(
                        "Know your audience",
                        HTML.p("This is the content for Know your audience.")
                    ),
                    AccordionSection(
                        "How people read",
                        HTML.p("This is the content for How people read.")
                    ),
                    css_id="accordion"
                )
            )

You can see this form live in the Demo site.

The first argument passed to the ``AccordionSection`` is the title, followed by the
list of fields or other layout objects that will shown in the section. You can add
any number of fields, other layout objects or composed layouts: ::

    ...
    self.helper.layout = Layout(
        Accordion(
            AccordionSection(
                "Profile", "name", "born"
            ),
            AccordionSection(
                "Contact", "email", Row(
                    "country_code", "phone_number", "extension"
                )
            ),
            css_id="accordion"
        )
    )

The ``css_id`` is needed for the Design System javascript to add all the CSS classes
and attributes that create the accordion. If there is only one accordion on a page you
`can` leave it out but, really, it's not recommended. What is likely to happen is that
a future release will add a default value so the extra typing can be avoided.
