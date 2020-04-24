.. _Fieldset: https://design-system.service.gov.uk/components/fieldset/

========
Fieldset
========
Use a `Fieldset`_  component to group related fields together. ::

    from django import forms

    from crispy_forms_gds.helper import FormHelper
    from crispy_forms_gds.layout import Field, Fieldset, Fluid, Layout, Size


        class FieldsetForm(forms.Form):

            street1 = forms.CharField(label="Building and street")
            street2 = forms.CharField(label="")
            city = forms.CharField(label="Town or city")
            county = forms.CharField(label="County")
            postcode = forms.CharField(label="Post code")

            def __init__(self, *args, **kwargs):
                super(FieldsetForm, self).__init__(*args, **kwargs)
                self.helper = FormHelper()
                self.helper.layout = Layout(
                    Fieldset(
                        Field.text("street1", field_width=Fluid.THREE_QUARTERS),
                        Field.text("street2", field_width=Fluid.THREE_QUARTERS),
                        Field.text("city", field_width=Fluid.ONE_HALF),
                        Field.text("county", field_width=Fluid.ONE_HALF),
                        Field.text("postcode", field_width=Fluid.ONE_QUARTER),
                        legend="What is your address?",
                        legend_size=Size.LARGE,
                        legend_tag="h1",
                    )
                )

You can see this form live in the Demo site.

Notice that the label on the ``street2`` field was set to an empty string. If you
simply don't set the label or set it to ``None`` Django will display the name of
field.

The positional arguments are the list of fields, other layout object or composed
layouts that make up the group. The ``Field.text()`` class method is used as it
simplifies setting the CSS class that defines the width of a field, for example
``govuk-!-width-three-quarters``. The Design System components are configured
using a mix of CSS classes, added attributes and template variables so the class
methods on ``Field`` and other layout classes make a life a lot easier.

The keyword arguments, ``legend``, ``legend_size`` and ``legend_tag`` are used to
define the legend for the fieldset. The ``legend`` attribute is obvious enough.
You will need to set the ``legend_size`` otherwise the legend will be the same size
as body text, which is a bit unimposing. The ``Size`` class defines a set of string
constants, ``SMALL``, ``MEDIUM``, ``LARGE`` and ``EXTRA_LARGE`` to make things a
little more readable but you can just use the corresponding values: ``'s'``, ``'m'``,
``'l'`` or ``'xl'`` directly if you prefer. The ``legend_tag`` argument is used to
promote the fieldset's ``<legend>`` element to become the page title. Typically a
Fieldset would be displayed as a single element on a multi-page form. Adding an
``<h1>`` element to the page would just add irritating duplication, particularly
for users of screen readers, so wrapping the legend in a heading tag avoids this.
You can wrap other tags as well. If you have two fieldsets on a page then it makes
sense to add a page title and wrap the fieldsets in an ``<h2>`` tag.
