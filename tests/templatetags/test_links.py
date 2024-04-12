"""
Tests to verify template tags for generating links are working.

"""

import os

from django.test.html import parse_html
from django.utils.safestring import SafeString

from crispy_forms_gds.templatetags.crispy_forms_gds import (
    back_link,
    button_link,
    button_start,
)
from tests.utils import TEST_DIR, parse_contents, parse_template

RESULT_DIR = os.path.join(TEST_DIR, "templatetags", "results")


def test_back_link():
    html = back_link("http://www.example.com/")
    assert isinstance(html, SafeString)
    assert parse_html(html) == parse_contents(RESULT_DIR, "back_link.html")


def test_button_link():
    html = button_link("http://www.example.com/", "Link")
    assert isinstance(html, SafeString)
    assert parse_html(html) == parse_contents(RESULT_DIR, "button_link.html")


def test_button_start():
    html = button_start("http://www.example.com/", "Start now")
    assert isinstance(html, SafeString)
    assert parse_html(html) == parse_contents(RESULT_DIR, "button_start.html")


def test_breadcrumbs():
    links = [
        ("Home", "/"),
        ("Previous", "/previous/"),
        ("Current", None),
    ]
    template = '{% include "gds/layout/breadcrumbs.html" %}'
    assert parse_template(template, crumbs=links) == parse_contents(
        RESULT_DIR, "breadcrumbs.html"
    )
