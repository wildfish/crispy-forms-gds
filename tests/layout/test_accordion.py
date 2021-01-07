"""
Tests to verify accordions are rendered correctly.

"""
import os

from crispy_forms_gds.layout import HTML, Accordion, AccordionSection, Layout
from tests.forms import AccordionForm
from tests.utils import TEST_DIR, parse_contents, parse_form

RESULT_DIR = os.path.join(TEST_DIR, "layout", "results", "accordion")


def test_basic_layout():
    """Verify all the gds attributes are displayed."""
    form = AccordionForm()
    assert parse_form(form) == parse_contents(RESULT_DIR, "layout.html")


def test_css_class():
    """Verify an extra CSS class can be added."""
    form = AccordionForm()
    form.helper.layout = Layout(Accordion(css_class="extra-css-class"))
    assert parse_form(form) == parse_contents(RESULT_DIR, "css_class.html")


def test_css_id():
    """Verify the accordion id can be set."""
    form = AccordionForm()
    form.helper.layout = Layout(Accordion(css_id="new-id"))
    assert parse_form(form) == parse_contents(RESULT_DIR, "css_id.html")


def test_attributes():
    """Verify extra attributes can be added."""
    form = AccordionForm()
    form.helper.layout = Layout(Accordion(key="value"))
    assert parse_form(form) == parse_contents(RESULT_DIR, "attributes.html")


def test_section_css_class():
    """Verify an extra CSS class can be added to an accordion section."""
    form = AccordionForm()
    form.helper.layout = Layout(
        Accordion(
            AccordionSection("Title", HTML("Contents"), css_class="extra-css-class")
        )
    )
    assert parse_form(form) == parse_contents(RESULT_DIR, "section_css_class.html")


def test_section_css_id():
    """Verify the accordion section id can be set."""
    form = AccordionForm()
    form.helper.layout = Layout(
        Accordion(AccordionSection("Title", HTML("Contents"), css_id="new_id"))
    )
    assert parse_form(form) == parse_contents(RESULT_DIR, "section_css_id.html")


def test_section_attributes():
    """Verify extra attributes can be added to an accordion section."""
    form = AccordionForm()
    form.helper.layout = Layout(
        Accordion(AccordionSection("Title", HTML("Contents"), key="value"))
    )
    assert parse_form(form) == parse_contents(RESULT_DIR, "section_attributes.html")
