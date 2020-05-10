"""
Tests to verify that Field objects are configured correctly.

"""
import pytest

from crispy_forms_gds.layout import Field, Fixed, Fluid, Size


def test_text_field_defaults():
    field = Field.text("name")
    assert field.context == {}
    assert field.attrs == {}


def test_text_field_label_size():
    field = Field.text("name", label_size=Size.MEDIUM)
    assert field.context["label_size"] == "govuk-label--m"
    assert field.attrs == {}


def test_text_invalid_label_size():
    with pytest.raises(ValueError):
        Field.text("name", label_size="other")


def test_text_field_fixed_width():
    field = Field.text("name", field_width=Fixed.TEN)
    assert field.attrs["class"] == "govuk-input--width-10"
    assert field.context == {}


def test_text_invalid_fixed_width():
    with pytest.raises(ValueError):
        Field.text("name", field_width=1)


def test_text_new_fixed_width():
    field = Field("name", css_class=Fixed.for_input(1, validate=False))
    assert field.attrs["class"] == "govuk-input--width-1"
    assert field.context == {}


def test_text_field_fluid_width():
    field = Field.text("name", field_width=Fluid.THREE_QUARTERS)
    assert field.attrs["class"] == "govuk-!-width-three-quarters"
    assert field.context == {}


def test_text_invalid_fluid_width():
    with pytest.raises(ValueError):
        Field.text("name", field_width="ninety-percent")


def test_text_new_fluid_width():
    field = Field("name", css_class=Fluid.for_input("one-fifth", validate=False))
    assert field.attrs["class"] == "govuk-!-width-one-fifth"
    assert field.context == {}
