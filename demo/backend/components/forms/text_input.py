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
