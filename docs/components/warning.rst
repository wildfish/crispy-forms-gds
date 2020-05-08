.. _Warning text: https://design-system.service.gov.uk/components/warning-text/

############
Warning text
############
A `Warning text`_ component is simply HTML. It's included as a form component as
warnings are useful for frightening your users into filling out the form
correctly. ::

    from django import forms

    from crispy_forms_gds.helper import FormHelper
    from crispy_forms_gds.layout import HTML, Layout


    class WarningForm(forms.Form):
        def __init__(self, *args, **kwargs):
            super(WarningForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(
                HTML.warning(
                    "You can be fined up to £5,000 if you do not like this template pack."
                )
            )

You can see this form live in the Demo site.

The styling and layout for a warning is not flexible. You could the symbol but
the styling is fixed so the symbol's background is black. Since a Warning component
is just a snippet of HTML it is much easier simply to clone the styling and generate
your own HTML if you need something different.
