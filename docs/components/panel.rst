=====
Panel
=====

Use a `Panel`_ component for confirmation messages or to highlight important sections.

.. _Panel: https://design-system.service.gov.uk/components/panel/


.. code-block::

    from django import forms

    from crispy_forms_gds.helper import FormHelper
    from crispy_forms_gds.layout import HTML, Layout


    class InsetForm(forms.Form):
        def __init__(self, *args, **kwargs):
            super(InsetForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(
                HTML.panel(
                    "Application complete",
                    "Your reference number <strong>HDJ2123F</strong>"
                )
            )


You can see this form live in the Demo site.

On the to-do list is to see if it is possible to change the background colour.
