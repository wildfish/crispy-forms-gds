.. _Details: https://design-system.service.gov.uk/components/details/

=======
Details
=======
A `Details`_ component is simply HTML. It's included as a form component as details
section are useful for adding extra, optional information such as help text to
fields. ::

    from django import forms

    from crispy_forms_gds.helper import FormHelper
    from crispy_forms_gds.layout import HTML, Layout


    class DetailsForm(forms.Form):
        def __init__(self, *args, **kwargs):
            super(DetailsForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(
                HTML.details(
                    "Help with nationality",
                    "We need to know your nationality so we can work out which "
                    "elections you’re entitled to vote in. If you cannot provide "
                    "your nationality, you’ll have to send copies of identity "
                    "documents through the post.",
                )
            )

You can see this form live in the Demo site.

What would be interesting would be to see if the Design System lets you add fields
instead of static contents. It is obviously a user experience nightmare but it is
something we might look into at a late time.
