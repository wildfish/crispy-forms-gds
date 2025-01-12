from crispy_forms_gds.choices import Choice


def test_set_attribute():
    """Verify an attribute can be set on a Choice after creation."""
    item = Choice("email", "Email")
    item.any = "An attribute"
    assert item.any == "An attribute"


def test_item_index():
    """Verify ChoiceItem supports indexing."""
    item = Choice("email", "Email", hint="Your email address")
    assert item[0] == "email"
    assert item[1] == "Email"


def test_iterator_unpacking():
    """Verify iterating over and unpacking a Choice returns the key and value."""
    choices = (Choice("email", "Email", hint="Your email address"),)
    for k, v in choices:
        assert k == "email"
        assert v == "Email"


def test_iterator_object():
    """Verify iterating over a Choice returns a ChoiceItem object."""
    choices = (
        Choice("email", "Email", hint="Your email address"),
        Choice("text", "Text", hint="Your mobile phone number"),
    )
    for item in choices:
        assert isinstance(item, Choice)
