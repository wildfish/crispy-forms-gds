.. _Text input: https://design-system.service.gov.uk/components/text-input/

==========
Text input
==========
The `Text input`_ component is the work-horse of any form: ::

    from django import forms


    from crispy_forms_gds.helper import FormHelper
    from crispy_forms_gds.layout import (
        Div,
        Layout,
        Field,
        Size,
        Fixed,
        Fluid,
        HTML,
        Fieldset,
    )


    class TextInputForm(forms.Form):

        name = forms.CharField(
            label="Event name",
            help_text="Enter the name of the event as it appears on the flyer.",
        )

        thirty = forms.CharField(label="30 character width")
        twenty = forms.CharField(label="20 character width")
        ten = forms.CharField(label="10 character width")
        five = forms.CharField(label="5 character width")
        four = forms.CharField(label="4 character width")
        three = forms.CharField(label="3 character width")
        two = forms.CharField(label="2 character width")

        full = forms.CharField(label="Full width")
        three_quarters = forms.CharField(label="Three-quarters width")
        two_thirds = forms.CharField(label="Two-thirds width")
        one_half = forms.CharField(label="One-half width")
        one_third = forms.CharField(label="One-third width")
        one_quarter = forms.CharField(label="One-quarter width")

        def __init__(self, *args, **kwargs):
            super(TextInputForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.legend_size = Size.SMALL
            self.helper.layout = Layout(
                Div(
                    Field.text("name", label_size=Size.SMALL, label_tag="h2"),
                    css_class="govuk-!-margin-bottom-9",
                ),
                Div(
                    HTML.h2("Use appropriately-sized text inputs"),
                    HTML.p(
                        "Help users understand what they should enter by making "
                        "text inputs the right size for the content they’re intended for."
                    ),
                ),
                Fieldset(
                    HTML.p(
                        "Use fixed width inputs for content that has a specific, "
                        "known length. Postcode inputs should be postcode-sized, "
                        "telephone number inputs should be telephone number-sized."
                    ),
                    Field.text("thirty", field_width=Fixed.THIRTY),
                    Field.text("twenty", field_width=Fixed.TWENTY),
                    Field.text("ten", field_width=Fixed.TEN),
                    Field.text("five", field_width=Fixed.FIVE),
                    Field.text("four", field_width=Fixed.FOUR),
                    Field.text("three", field_width=Fixed.THREE),
                    Field.text("two", field_width=Fixed.TWO),
                    legend="Fixed width inputs",
                    legend_size=Size.MEDIUM,
                    legend_tag="h2",
                ),
                Fieldset(
                    HTML.p(
                        "Use the width override classes to reduce the width of an "
                        "input in relation to its parent container, for example, "
                        "to two-thirds."
                    ),
                    Field.text("full", field_width=Fluid.FULL),
                    Field.text("three_quarters", field_width=Fluid.THREE_QUARTERS),
                    Field.text("two_thirds", field_width=Fluid.TWO_THIRDS),
                    Field.text("one_half", field_width=Fluid.ONE_HALF),
                    Field.text("one_third", field_width=Fluid.ONE_THIRD),
                    Field.text("one_quarter", field_width=Fluid.ONE_QUARTER),
                    legend="Fluid width inputs",
                    legend_size=Size.MEDIUM,
                    legend_tag="h2",
                ),
            )

You can see this form live in the Demo site.

You might think that we went a little overboard with this as an example, but with
a little more effort we could have essentially cloned the entire content of the
`Text input`_ page from the GOV.UK Design System site - all within the form.

The only thing unique to Text inputs is that you can set the width so the field
is sized appropriately. The other features like setting the ``label_size`` and
``label_tag`` has been covered in the other components. It should be self-explanatory
if you have not seen it before.

Two things of note that are not covered elsewhere. You can set default sizes on the
``FormHelper`` instance. Here we set a default size for all ``<legend>`` elemennts
to small ('s'). This can then be overridden on each element that has a legend on a
case-by-case basis. The second thing not used else where is passing CSS classes on
layout objects. The first ``Div`` has margin added to inject some space before the
section on widths.

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

