.. _fixed width or fluid width fields: https://design-system.service.gov.uk/components/text-input/#use-appropriately-sized-text-inputs

#################################
Changing the size of a Text input
#################################
Text inputs, by default, take up the full width of the parent container. The
Design System supports either `fixed width or fluid width fields`_.

Use fixed widths whenever the content has a known length. Fields can be either:
2, 3, 4, 5, 10, 20 or 30 characters wide. The Design System has CSS classes
defined for each size, e.g. `govuk-input--width-5`.

Fluid widths are relative to the size of the parent container and are great when
you just need something smaller. Available sizes are: 'one-quarter', 'one-third',
'one-half', 'two-thirds', 'three-quarters' or finally, 'full'. Again there is a
separate CSS class for each size, e.g. `govuk-!-width-one-third`.

The easiest way to set the width for a Text input is to use the ``Field.text()``
method: ::

    from django import forms

    from crispy_forms_gds.helper import FormHelper
    from crispy_forms_gds.layout import Field, Fixed, Layout, Submit


    class CookbookForm(forms.Form):
        name = forms.CharField(label="Name")

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(
                Field.text("name", field_width=Fixed.FIVE),
                Submit("submit", "Submit")
            )

Fluid widths work exactly the same way: ::

    from django import forms

    from crispy_forms_gds.helper import FormHelper
    from crispy_forms_gds.layout import Field, Fluid, Layout, Submit


    class CookbookForm(forms.Form):
        name = forms.CharField(label="Name")

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(
                Field.text("name", field_width=Fluid.ONE_HALF),
                Submit("submit", "Submit")
            )

The class method maps the values from Fixed or Fluid to the respective CSS class
and adds it to the field. If you work with ``Fields`` directly then you will have
to do that yourself: ::

    from django import forms

    from crispy_forms_gds.helper import FormHelper
    from crispy_forms_gds.layout import Field, Layout, Submit


    class CookbookForm(forms.Form):
        name = forms.CharField(label="Name")

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(
                Field("name", css_class="govuk-input--width-5"),
                Submit("submit", "Submit")
            )

You don't have to use the constants defined in the ``Fixed`` or ``Fluid`` classes.
You can always set the values, e.g. 'm' directly. If you do this in the ``text()``
class method the value is checked to see if it is valid so you're less likely to
make a mistake. That might be a problem if the Design System adds more sizes but
this package takes some time to catch up. In that case you will need to see the
css class on the ``Field`` instance yourself.
