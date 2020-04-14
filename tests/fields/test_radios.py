"""
Tests to verify radio buttons are rendered correctly.

"""
import os

from tests.forms import RadiosForm
from tests.utils import TEST_DIR, parse_form, parse_contents

RESULT_DIR = os.path.join(TEST_DIR, "fields", "results", "radios")


def test_initial_attributes():
    """Verify all the gds attributes are displayed."""
    form = RadiosForm()
    assert parse_form(form) == parse_contents(RESULT_DIR, "initial.html")


def test_validation_error_attributes():
    """Verify all the gds error attributes are displayed."""
    form = RadiosForm(data={"method": ""})
    assert not form.is_valid()
    assert parse_form(form) == parse_contents(RESULT_DIR, "validation_errors.html")
