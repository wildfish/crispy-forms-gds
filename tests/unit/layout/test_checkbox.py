"""
Tests to verify a single (boolean) checkbox is rendered correctly.

"""

import os

import django

from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import Field, Layout
from tests.unit.forms import CheckboxForm
from tests.unit.utils import TEST_DIR, parse_contents, parse_form

RESULT_DIR = os.path.join(TEST_DIR, "layout", "results", "checkbox")


def test_initial_attributes():
    """Verify all the gds attributes are displayed."""
    form = CheckboxForm(initial={"accept": True})
    assert parse_form(form) == parse_contents(RESULT_DIR, "initial.html")


def test_validation_error_attributes():
    """Verify all the gds error attributes are displayed."""
    form = CheckboxForm(data={"accept": ""})
    assert not form.is_valid()
    if django.VERSION[0] < 5:
        template = "validation_errors.html"
    else:
        template = "validation_errors_aria_invalid.html"
    assert parse_form(form) == parse_contents(RESULT_DIR, template)


def test_checkbox_size():
    """Verify size of the checkbox can be changed from the default."""
    form = CheckboxForm()
    form.helper = FormHelper()
    form.helper.layout = Layout(Field("accept", context={"checkboxes_small": True}))
    assert parse_form(form) == parse_contents(RESULT_DIR, "checkbox_size.html")


def test_no_help_text():
    """Verify field is rendered correctly if no help text is given."""
    form = CheckboxForm()
    form.fields["accept"].help_text = ""
    assert parse_form(form) == parse_contents(RESULT_DIR, "no_help_text.html")


def test_no_help_text_errors():
    """Verify all the gds error attributes are displayed if no help text is given."""
    form = CheckboxForm(data={"accept": ""})
    form.fields["accept"].help_text = ""
    if django.VERSION[0] < 5:
        template = "no_help_text_errors.html"
    else:
        template = "no_help_text_errors_aria_invalid.html"
    assert parse_form(form) == parse_contents(RESULT_DIR, template)
