"""
Tests to verify fieldsets are rendered correctly.

"""
import os

from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import Fieldset, Layout, Size
from tests.forms import FieldsetForm
from tests.utils import TEST_DIR, parse_contents, parse_form

RESULT_DIR = os.path.join(TEST_DIR, "layout", "results", "fieldset")


def test_basic_layout():
    """Verify all the gds attributes are displayed."""
    form = FieldsetForm()
    assert parse_form(form) == parse_contents(RESULT_DIR, "layout.html")


def test_show_legend_as_heading():
    """Verify the field legend can be displayed as the page heading."""
    form = FieldsetForm()
    form.helper = FormHelper()
    form.helper.layout = Layout(
        Fieldset("name", "email", legend="Contact", legend_tag="h1")
    )
    assert parse_form(form) == parse_contents(RESULT_DIR, "legend_heading.html")


def test_change_legend_size():
    """Verify size of the field legend can be changed from the default."""
    form = FieldsetForm()
    form.helper = FormHelper()
    form.helper.layout = Layout(
        Fieldset("name", "email", legend="Contact", legend_size=Size.LARGE)
    )
    assert parse_form(form) == parse_contents(RESULT_DIR, "legend_size.html")


def test_css_class():
    """Verify an extra CSS class can be added to the fieldset."""
    form = FieldsetForm()
    form.helper = FormHelper()
    form.helper.layout = Layout(Fieldset(css_class="extra-css-class"))
    assert parse_form(form) == parse_contents(RESULT_DIR, "css_class.html")


def test_css_id():
    """Verify the id attribute can be set on the fieldset."""
    form = FieldsetForm()
    form.helper = FormHelper()
    form.helper.layout = Layout(Fieldset(css_id="new_id"))
    assert parse_form(form) == parse_contents(RESULT_DIR, "css_id.html")


def test_attribute():
    """Verify the extra attributes can be added."""
    form = FieldsetForm()
    form.helper = FormHelper()
    form.helper.layout = Layout(Fieldset(key="value"))
    assert parse_form(form) == parse_contents(RESULT_DIR, "attributes.html")
