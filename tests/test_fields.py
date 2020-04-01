"""
Tests to verify the different types of field are rendered correctly.

Each test creates a from with a single field of the target type. The
form is initialized with invalid (submitted) data so a validation
error will be displayed when the form is rendered. This ensures that
all the GDS related attributes on the various element will be displayed.

"""

from django.test.html import parse_html

from tests.forms import TextInputForm
from tests.utils import render_form, expected_results


def test_text_input():
    form = TextInputForm(data={"field_name": ""})
    assert not form.is_valid()
    actual = render_form(form)
    expected = expected_results("forms", "test_text_input.html")
    assert parse_html(actual) == parse_html(expected)
