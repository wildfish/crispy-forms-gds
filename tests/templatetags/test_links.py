"""
Tests to verify template tags for generating links are working.

"""
import os

from django.test.html import parse_html
from django.utils.safestring import SafeString

from crispy_forms_gds.templatetags.crispy_forms_gds import back_link, button_link
from tests.utils import TEST_DIR, parse_contents


RESULT_DIR = os.path.join(TEST_DIR, "templatetags", "results")


def test_back_link():
    html = back_link("http://www.example.com/")
    assert isinstance(html, SafeString)
    assert parse_html(html) == parse_contents(RESULT_DIR, "back_link.html")


def test_button_link():
    html = button_link("http://www.example.com/", "Link")
    assert isinstance(html, SafeString)
    assert parse_html(html) == parse_contents(RESULT_DIR, "button_link.html")