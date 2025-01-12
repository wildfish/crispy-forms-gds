import os

from tests.unit.forms import ConditionalRadiosForm
from tests.unit.utils import TEST_DIR, parse_contents, parse_form

RESULT_DIR = os.path.join(TEST_DIR, "layout", "results", "conditional_radios")


def test_conditional_radios():
    """Verify the HTML for conditional radios"""
    form = ConditionalRadiosForm()
    assert parse_form(form) == parse_contents(RESULT_DIR, "conditional_radios.html")
