"""
Tests to verify that Field objects are rendered correctly.

"""
from crispy_forms_gds.layout import Field


def test_wrapper_class_is_added_to_context():
    """Verify that if wrapper_class is listed in the kwargs it is added to the
    extra_context so it will be available in the template."""
    field = Field("name", wrapper_class="wrapper")
    assert field.extra_context["wrapper_class"] == "wrapper"
