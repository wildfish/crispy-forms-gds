import io
import os

from django.conf import settings as django_settings
from django.template import Context, Template


from . import settings


TEST_DIR = os.path.dirname(os.path.abspath(__file__))


def configure_django(**kwargs):
    """
    Configure Django with all the settings defined in tests/settings.py.
    """
    values = {k: getattr(settings, k) for k in dir(settings) if k.isupper()}
    values.update(kwargs)
    django_settings.configure(**values)


def file_contents(path):
    with io.open(path, "r", encoding="utf-8") as fp:
        return fp.read()


def expected_results(*args):
    return file_contents(os.path.join(TEST_DIR, "expected", *args))


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
