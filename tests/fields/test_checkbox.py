"""
Tests to verify checkboxes are rendered correctly.

"""
import os

from tests.forms import CheckboxForm
from tests.utils import TEST_DIR, parse_contents, parse_form


RESULT_DIR = os.path.join(TEST_DIR, "fields", "results", "checkbox")


def test_initial_attributes():
    """Verify all the gds attributes are displayed."""
    form = CheckboxForm()
    assert parse_form(form) == parse_contents(RESULT_DIR, "initial.html")


def test_validation_error_attributes():
    """Verify all the gds error attributes are displayed."""
    form = CheckboxForm(data={"accept": ""})
    assert not form.is_valid()
    assert parse_form(form) == parse_contents(RESULT_DIR, "validation_errors.html")


def test_no_help_text():
    """Verify field is rendered correctly if no help text is given."""
    form = CheckboxForm()
    form.fields["accept"].help_text = ""
    assert parse_form(form) == parse_contents(RESULT_DIR, "no_help_text.html")


def test_no_help_text_errors():
    """Verify all the gds error attributes are displayed if no help text is given."""
    form = CheckboxForm(data={"accept": ""})
    form.fields["accept"].help_text = ""
    assert parse_form(form) == parse_contents(RESULT_DIR, "no_help_text_errors.html")
