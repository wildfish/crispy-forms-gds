"""
Tests to verify text fields are rendered correctly.

"""
import os

from tests.forms import ButtonsForm
from tests.utils import TEST_DIR, parse_form, parse_contents

RESULT_DIR = os.path.join(TEST_DIR, "fields", "results", "buttons")


def test_initial_attributes():
    """Verify all the gds attributes are displayed."""
    form = ButtonsForm()
    assert parse_form(form) == parse_contents(RESULT_DIR, "initial.html")
