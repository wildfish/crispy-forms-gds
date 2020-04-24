"""
Tests to verify text fields are rendered correctly.

"""
import os

from django.test.html import parse_html

from tests.forms import TextInputForm
from tests.utils import TEST_DIR, parse_contents, render_template


RESULT_DIR = os.path.join(TEST_DIR, "helpers", "results")


def test_error_summary():
    """Verify an error summary is displayed correctly."""
    template = """
        {% load crispy_forms_tags %}
        {% if form.helper.form_show_errors and form.errors %}
          {% include 'gds/layout/error_summary.html' %}
        {% endif %}
        <div class="govuk-body">
        {% crispy form %}
        </div>
    """
    form = TextInputForm(data={"name": ""})
    form.add_error(None, "Non-field error")
    page = render_template(template, form=form)
    assert parse_html(page) == parse_contents(RESULT_DIR, "error_summary.html")
