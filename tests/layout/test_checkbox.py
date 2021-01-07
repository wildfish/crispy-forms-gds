"""
Tests to verify a single (boolean) checkbox is rendered correctly.

"""
import os

from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import Field, Layout
from tests.forms import CheckboxForm
from tests.utils import TEST_DIR, parse_contents, parse_form

RESULT_DIR = os.path.join(TEST_DIR, "layout", "results", "checkbox")


def test_initial_attributes():
    """Verify all the gds attributes are displayed."""
    form = CheckboxForm(initial={"accept": True})
    assert parse_form(form) == parse_contents(RESULT_DIR, "initial.html")


def test_validation_error_attributes():
    """Verify all the gds error attributes are displayed."""
    form = CheckboxForm(data={"accept": ""})
    assert not form.is_valid()
    assert parse_form(form) == parse_contents(RESULT_DIR, "validation_errors.html")


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
    assert parse_form(form) == parse_contents(RESULT_DIR, "no_help_text_errors.html")
