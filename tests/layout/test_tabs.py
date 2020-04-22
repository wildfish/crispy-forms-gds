"""
Tests to verify selects are rendered correctly.

"""
import os

from tests.forms import TabsForm
from tests.utils import TEST_DIR, parse_form, parse_contents

RESULT_DIR = os.path.join(TEST_DIR, "layout", "results", "tabs")


def test_basic_layout():
    """Verify all the gds attributes are displayed.

    Note: when the tabs are rendered a lot of extra markup is added so the
    template only contains the basic HTML to get the component to work. When
    you inspect the content in a browser it will look quite different.
    """
    form = TabsForm()
    assert parse_form(form) == parse_contents(RESULT_DIR, "layout.html")
