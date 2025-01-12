"""
Tests to verify selects are rendered correctly.

"""

import os

import django

from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import Field, Layout, Size
from tests.unit.forms import SelectForm
from tests.unit.utils import TEST_DIR, parse_contents, parse_form

RESULT_DIR = os.path.join(TEST_DIR, "layout", "results", "select")


def test_initial_attributes():
    """Verify all the gds attributes are displayed."""
    form = SelectForm(initial={"method": "email"})
    assert parse_form(form) == parse_contents(RESULT_DIR, "initial.html")


def test_validation_error_attributes():
    """Verify all the gds error attributes are displayed."""
    form = SelectForm(data={"method": ""})
    assert not form.is_valid()
    if django.VERSION[0] < 5:
        template = "validation_errors.html"
    else:
        template = "validation_errors_aria_invalid.html"
    assert parse_form(form) == parse_contents(RESULT_DIR, template)


def test_show_label_as_heading():
    """Verify the field label can be displayed as the page heading."""
    form = SelectForm()
    form.helper = FormHelper()
    form.helper.layout = Layout(Field("method", context={"label_tag": "h1"}))
    assert parse_form(form) == parse_contents(RESULT_DIR, "label_heading.html")


def test_change_label_size():
    """Verify size of the field label can be changed from the default."""
    form = SelectForm()
    form.helper = FormHelper()
    form.helper.layout = Layout(
        Field("method", context={"label_size": Size.for_label("l")})
    )
    assert parse_form(form) == parse_contents(RESULT_DIR, "label_size.html")


def test_no_label():
    """Verify field is rendered correctly if no label is given."""
    form = SelectForm()
    form.fields["method"].label = ""
    assert parse_form(form) == parse_contents(RESULT_DIR, "no_label.html")


def test_no_help_text():
    """Verify field is rendered correctly if no help text is given."""
    form = SelectForm()
    form.fields["method"].help_text = ""
    assert parse_form(form) == parse_contents(RESULT_DIR, "no_help_text.html")


def test_no_help_text_errors():
    """Verify all the gds error attributes are displayed if no help text is given."""
    form = SelectForm(data={"method": ""})
    form.fields["method"].help_text = ""
    if django.VERSION[0] < 5:
        template = "no_help_text_errors.html"
    else:
        template = "no_help_text_errors_aria_invalid.html"
    assert parse_form(form) == parse_contents(RESULT_DIR, template)
