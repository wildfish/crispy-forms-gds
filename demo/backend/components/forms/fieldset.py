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
                title="What is your address?",
                size=Size.LARGE,
                tag="h1",
            )
        )
