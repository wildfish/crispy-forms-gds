import io
import os

import django

from django.conf import settings as django_settings
from django.template import Context, Template
from django.test.html import parse_html


from . import settings


TEST_DIR = os.path.dirname(os.path.abspath(__file__))


def configure_django(**kwargs):
    """
    Configure Django with all the settings defined in tests/settings.py.
    """
    values = {k: getattr(settings, k) for k in dir(settings) if k.isupper()}
    values.update(kwargs)
    django_settings.configure(**values)
    django.setup()


def get_contents(*args):
    with io.open(os.path.join(*args), "r", encoding="utf-8") as fp:
        return fp.read()


def parse_contents(*args):
    return parse_html(get_contents(*args))


def render_form(form, **kwargs):
    """
    Render a form using a Django Template
    """
    context = Context(kwargs)
    context["form"] = form
    tpl = """
        {% load crispy_forms_tags %}
        {% crispy form %}
    """
    return Template(tpl).render(context)


def parse_form(form):
    return parse_html(render_form(form))
