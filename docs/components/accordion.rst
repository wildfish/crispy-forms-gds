.. _Accordion: https://design-system.service.gov.uk/components/accordion/

#########
Accordion
#########
There are two Layout classes for adding an `Accordion`_ to a form. ``AccordionSection``
which wraps the contents of each section and ``Accordion`` which wraps the sections
and adds the ability to open and collapse them.

.. code-block::django

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
                        summary="An introduction to clear and concise writing.",
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
                    )
                )
            )

You can see this form live in the Demo site.

The first argument passed to the ``AccordionSection`` is the title, followed by the
list of fields or other layout objects that will shown in the section. You can add
any number of fields, other layout objects or composed layouts:

.. code-block::django

    Accordion(
        AccordionSection(
            "Contact", "email", Div(
                "country_code", "phone_number", "extension"
            )
        )
    )


There is also the optional ``summary`` keyword argument. This is a short description
of the contents of a panel so the user does not need to open it:

.. code-block::django

    AccordionSection(
        "Writing well for the web",
        HTML.p("This is the content for Writing well for the web.")
        summary="An introduction to clear and concise writing.",
    ),


Each ``Accordion`` on a page needs to have a unique identifier otherwise the javascript
used to control the component will not function correctly. You set the identifier using
the ``css_id`` keyword argument: ::

    Accordion(
        AccordionSection(
            ...
        ),
        css_id="accordion-1"
    ),
    ...
    Accordion(
        AccordionSection(
            ...
        ),
        css_id="accordion-2"
    )

The default value is ``accordion``. Tf there is only one accordion on the page you
don't need to change it.

You cannot nest Accordions. Firstly because the javascript controls don't work - all
the panels are open. Secondly, it's visually confusing. The nested Accordion is not
indented.
