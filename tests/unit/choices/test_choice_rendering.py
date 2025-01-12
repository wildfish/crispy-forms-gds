from django.template import Context, Template

from crispy_forms_gds.choices import Choice


def test_item_index_lookup():
    """Verify choice item supporting indexing in template."""
    choices = (Choice("email", "Email", hint="Your email address"),)
    template = "{% for choice in choices %}{{ choice.0 }} {{ choice.1 }}{% endfor %}"
    result = Template(template).render(Context({"choices": choices}))
    assert result == "email Email"


def test_item_hint_lookup():
    """Verify choice item hint lookup in template."""
    choices = (Choice("email", "Email", hint="Your email address"),)
    template = "{% for choice in choices %}{% if choice.hint %}{{ choice.hint }}{% endif %}{% endfor %}"  # noqa
    result = Template(template).render(Context({"choices": choices}))
    assert result == "Your email address"


def test_item_divider_lookup():
    """Verify choice item hint lookup in template."""
    choices = (Choice("email", "Email", divider="Or"),)
    template = "{% for choice in choices %}{% if choice.divider %}{{ choice.divider }}{% endif %}{% endfor %}"  # noqa
    result = Template(template).render(Context({"choices": choices}))
    assert result == "Or"


def test_tuple_index_lookup():
    """Verify index lookup - this exists in Django and is included for symmetry."""
    choices = (("email", "Email"),)
    template = "{% for choice in choices %}{{ choice.0 }} {{ choice.1 }}{% endfor %}"
    result = Template(template).render(Context({"choices": choices}))
    assert result == "email Email"


def test_tuple_hint_lookup():
    """Verify hint lookup on a tuple does not trigger an error."""
    choices = (("email", "Email"),)
    template = "{% for choice in choices %}{% if choice.hint %}{{ choice.hint }}{% endif %}{% endfor %}"  # noqa
    result = Template(template).render(Context({"choices": choices}))
    assert result == ""
