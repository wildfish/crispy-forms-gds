"""
Tests to verify tables are rendered correctly.

"""
import os

import pytest

from crispy_forms_gds.layout import HTML
from tests.forms import TableForm
from tests.utils import TEST_DIR, parse_contents, parse_form

RESULT_DIR = os.path.join(TEST_DIR, "layout", "results", "table")


def test_basic_layout():
    """Verify all the gds attributes are displayed."""
    form = TableForm()
    assert parse_form(form) == parse_contents(RESULT_DIR, "layout.html")


@pytest.mark.parametrize(
    "headers,rows,caption,header_css,row_css",
    [
        (["Title"], [["Cell"]], "Caption", ["header-css-class"], ["row-css-class"]),
        ([], [["Cell"]], "Caption", ["header-css-class"], ["row-css-class"]),
        (["Title"], [[]], "Caption", ["header-css-class"], ["row-css-class"]),
        (["Title"], [["Cell"]], "", ["header-css-class"], ["row-css-class"]),
        (["Title"], [["Cell"]], None, ["header-css-class"], ["row-css-class"]),
        (["Title"], [["Cell"]], "Caption", [], ["row-css-class"]),
        (["Title"], [["Cell"]], "Caption", None, ["row-css-class"]),
        (["Title"], [["Cell"]], "Caption", ["header-css-class"], []),
        (["Title"], [["Cell"]], "Caption", ["header-css-class"], None),
    ],
)
def test_parameters(headers, rows, caption, header_css, row_css):
    field = HTML.table(
        headers, rows, caption=caption, header_css=header_css, row_css=row_css
    )
    assert isinstance(field, HTML)
