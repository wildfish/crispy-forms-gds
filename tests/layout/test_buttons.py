"""
Tests to verify buttons are rendered correctly.

"""
import os

from crispy_forms_gds.layout import Button
from tests.utils import TEST_DIR, parse_contents, parse_template


RESULT_DIR = os.path.join(TEST_DIR, "layout", "results", "buttons")
TEMPLATE = '{% include "gds/layout/button.html" %}'


def test_primary_button():
    button = Button.primary("name", "Title")
    assert parse_template(TEMPLATE, input=button) == parse_contents(
        RESULT_DIR, "primary.html"
    )


def test_secondary_button():
    button = Button.secondary("name", "Title")
    assert parse_template(TEMPLATE, input=button) == parse_contents(
        RESULT_DIR, "secondary.html"
    )


def test_warning_button():
    button = Button.warning("name", "Title")
    assert parse_template(TEMPLATE, input=button) == parse_contents(
        RESULT_DIR, "warning.html"
    )


def test_disabled_button():
    button = Button.primary("name", "Title", disabled=True)
    assert parse_template(TEMPLATE, input=button) == parse_contents(
        RESULT_DIR, "disabled.html"
    )
