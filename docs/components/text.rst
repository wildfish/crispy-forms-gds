.. _Text input: https://design-system.service.gov.uk/components/text-input/

##########
Text input
##########
The `Text input`_ component is the work-horse of any form: ::

    from django import forms

    from crispy_forms_gds.helper import FormHelper
    from crispy_forms_gds.layout import (
        Field,
        Fieldset,
        Fixed,
        Fluid,
        Layout,
        Size,
        Submit,
    )


    class TextInputForm(forms.Form):

        name = forms.CharField(
            label="Your name", help_text="Enter your name as it appears on your passport.",
        )

        email = forms.CharField(label="Email", help_text="Enter your email address.",)

        phone = forms.CharField(
            label="Phone", help_text="Enter your home or mobile telephone number.",
        )

        def __init__(self, *args, **kwargs):
            super(TextInputForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.label_size = Size.SMALL
            self.helper.layout = Layout(
                Fieldset(
                    Field.text("name"),
                    Field.text("email", field_width=Fluid.TWO_THIRDS),
                    Field.text("phone", field_width=Fixed.TEN),
                ),
                Submit("submit", "Submit"),
            )

You can see this form live in the Demo site.

You can set default sizes for labels and legands on the ``FormHelper`` instance.
Here we set a default size for all ``<label>`` elements to small ('m'). This can
then be overridden on each element that has a legend on a case-by-case basis.

The widths themselves use all the available constants defined on hte ``Fixed`` and
``Fluid`` classes: ::

    Field.text("ten", field_width=FIXED.TEN),
    Field.text("one_quarter", field_width=Fluid.ONE_QUARTER),

You could just use the values directly: ::

    Field.text("ten", field_width=10),
    Field.text("one_quarter", field_width="one-quarter"),

The code in the ``Field`` class checks to see the value is valid. In the event a
new width is added to the Design System and this template pack has not been updated
you can always pass in the relevant CSS class directly: ::

    Field("ten", css_class="govuk-input--width-10"),
    Field("one_quarter", css_class="govuk-!-width-one-quarter"),

