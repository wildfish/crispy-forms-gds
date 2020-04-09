"""
Tests to verify text fields are rendered correctly.

"""
import os

from tests.forms import TextInputForm
from tests.utils import TEST_DIR, parse_form, parse_contents

RESULT_DIR = os.path.join(TEST_DIR, "fields", "results", "text_input")


def test_initial_attributes():
    """Verify all the gds attributes are displayed."""
    form = TextInputForm()
    assert parse_form(form) == parse_contents(RESULT_DIR, "initial.html")


def test_validation_error_attributes():
    """Verify all the gds error attributes are displayed."""
    form = TextInputForm(data={"field_name": ""})
    assert not form.is_valid()
    assert parse_form(form) == parse_contents(RESULT_DIR, "validation_errors.html")


def test_set_fixed_width_with_integer():
    """Verify text fields can be set to be a fixed width using an integer."""
    form = TextInputForm()
    form.fields["name"].widget.attrs["width"] = 4
    assert parse_form(form) == parse_contents(RESULT_DIR, "fixed_width.html")


def test_set_relative_width():
    """Verify text fields can be set to be a width relative to their parent."""
    form = TextInputForm()
    form.fields["name"].widget.attrs["width"] = "one-quarter"
    assert parse_form(form) == parse_contents(RESULT_DIR, "relative_width.html")


def test_set_unsupported_fixed_width():
    """Verify new fixed width classes can be supported."""
    form = TextInputForm()
    form.fields["name"].widget.attrs["width"] = 25
    assert parse_form(form) == parse_contents(
        RESULT_DIR, "unsupported_fixed_width.html"
    )


def test_set_unsupported_relative_width():
    """Verify new relative width classes can be supported."""
    form = TextInputForm()
    form.fields["name"].widget.attrs["width"] = "four-fifths"
    assert parse_form(form) == parse_contents(
        RESULT_DIR, "unsupported_relative_width.html"
    )


def test_spellcheck_enabled():
    """Verify enabling spellchecking with True."""
    form = TextInputForm()
    form.fields["name"].widget.attrs["spellcheck"] = True
    assert parse_form(form) == parse_contents(RESULT_DIR, "spellcheck_enabled.html")


def test_spellcheck_disabled():
    """Verify disabling spellchecking with False."""
    form = TextInputForm()
    form.fields["name"].widget.attrs["spellcheck"] = False
    assert parse_form(form) == parse_contents(RESULT_DIR, "spellcheck_disabled.html")
