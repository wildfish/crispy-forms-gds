"""
Tests to verify tabs are rendered correctly.

"""

import os

from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import Layout, TabPanel, Tabs
from tests.forms import TabsForm
from tests.utils import TEST_DIR, parse_contents, parse_form

RESULT_DIR = os.path.join(TEST_DIR, "layout", "results", "tabs")


def test_basic_layout():
    """Verify all the gds attributes are displayed.

    Note: when the tabs are rendered a lot of extra markup is added so the
    template only contains the basic HTML to get the component to work. When
    you inspect the content in a browser it will look quite different.
    """
    form = TabsForm()
    assert parse_form(form) == parse_contents(RESULT_DIR, "layout.html")


def test_css_class():
    """Verify an extra CSS class can be added to the parent div."""
    form = TabsForm()
    form.helper = FormHelper()
    form.helper.layout = Layout(Tabs(css_class="extra-css-class"))
    assert parse_form(form) == parse_contents(RESULT_DIR, "css_class.html")


def test_css_id():
    """Verify the id attribute can be set on the parent div."""
    form = TabsForm()
    form.helper = FormHelper()
    form.helper.layout = Layout(Tabs(css_id="new_id"))
    assert parse_form(form) == parse_contents(RESULT_DIR, "css_id.html")


def test_attribute():
    """Verify the extra attributes can be added to the parent div."""
    form = TabsForm()
    form.helper = FormHelper()
    form.helper.layout = Layout(Tabs(key="value"))
    assert parse_form(form) == parse_contents(RESULT_DIR, "attributes.html")


def test_panel_css_class():
    """Verify an extra CSS class can be added to a tab panel."""
    form = TabsForm()
    form.helper = FormHelper()
    form.helper.layout = Layout(Tabs(TabPanel("Title", css_class="extra-css-class")))
    assert parse_form(form) == parse_contents(RESULT_DIR, "panel_css_class.html")


def test_panel_css_id():
    """Verify the id attribute can be set on a tab panel."""
    form = TabsForm()
    form.helper = FormHelper()
    form.helper.layout = Layout(Tabs(TabPanel("Title", css_id="new_id")))
    assert parse_form(form) == parse_contents(RESULT_DIR, "panel_css_id.html")


def test_panel_attribute():
    """Verify the extra attributes can be added to a tab panel."""
    form = TabsForm()
    form.helper = FormHelper()
    form.helper.layout = Layout(Tabs(TabPanel("Title", key="value")))
    assert parse_form(form) == parse_contents(RESULT_DIR, "panel_attributes.html")
