.. _Inset text: https://design-system.service.gov.uk/components/inset-text/

##########
Inset text
##########
An `Inset text`_ component is simply HTML. It's included as a form component
so you can notes or side-comments to the body of a form. ::

    from django import forms

    from crispy_forms_gds.helper import FormHelper
    from crispy_forms_gds.layout import HTML, Layout


    class InsetForm(forms.Form):
        def __init__(self, *args, **kwargs):
            super(InsetForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(
                HTML.inset(
                    "It can take up to 8 weeks to register a lasting power of "
                    "attorney if there are no mistakes in the application. "
                )
            )

You can see this form live in the Demo site.
