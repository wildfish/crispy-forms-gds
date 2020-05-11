"""
Tests to verify tables are rendered correctly.

"""
import os

from tests.forms import TableForm
from tests.utils import TEST_DIR, parse_contents, parse_form


RESULT_DIR = os.path.join(TEST_DIR, "layout", "results", "table")


def test_basic_layout():
    """Verify all the gds attributes are displayed."""
    form = TableForm()
    assert parse_form(form) == parse_contents(RESULT_DIR, "layout.html")
