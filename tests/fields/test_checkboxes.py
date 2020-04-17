"""
Tests to verify checkboxes are rendered correctly.

"""
import os

from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import Field, Layout

from tests.forms import CheckboxesForm
from tests.utils import TEST_DIR, parse_form, parse_contents

RESULT_DIR = os.path.join(TEST_DIR, "fields", "results", "checkboxes")


def test_initial_attributes():
    """Verify all the gds attributes are displayed."""
    form = CheckboxesForm()
    assert parse_form(form) == parse_contents(RESULT_DIR, "initial.html")


def test_validation_error_attributes():
    """Verify all the gds error attributes are displayed."""
    form = CheckboxesForm(data={"method": ""})
    assert not form.is_valid()
    assert parse_form(form) == parse_contents(RESULT_DIR, "validation_errors.html")


def test_show_legend_as_heading():
    """Verify the field legend can be displayed as the page heading."""
    form = CheckboxesForm()
    form.helper = FormHelper()
    form.helper.layout = Layout(
        Field("method", extra_context=dict(field_label_is_heading=True))
    )
    assert parse_form(form) == parse_contents(RESULT_DIR, "legend_heading.html")


def test_change_legend_size():
    """Verify size of the field legend can be changed from the default."""
    form = CheckboxesForm()
    form.helper = FormHelper()
    form.helper.layout = Layout(
        Field("method", extra_context=dict(field_label_size="l"))
    )
    assert parse_form(form) == parse_contents(RESULT_DIR, "legend_size.html")
