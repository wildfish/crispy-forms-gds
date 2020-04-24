from django import forms

from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import HTML, Layout, Tabs, TabPanel


class TabsForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(TabsForm, self).__init__(*args, **kwargs)

        headings = ["Case manager", "Cases opened", "Cases closed"]
        past_day = [
            ["David Francis", "3", "0"],
            ["Paul Farmer", "1", "0"],
            ["Rita Patel", "2", "0"],
        ]
        past_week = [
            ["David Francis", "24", "18"],
            ["Paul Farmer", "16", "20"],
            ["Rita Patel", "24", "27"],
        ]
        past_month = [
            ["David Francis", "98", "95"],
            ["Paul Farmer", "122", "131"],
            ["Rita Patel", "126", "142"],
        ]
        past_year = [
            ["David Francis", "1380", "1472"],
            ["Paul Farmer", "1129", "1083"],
            ["Rita Patel", "1539", "1265"],
        ]

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Tabs(
                TabPanel(
                    "Past day", HTML.h1("Past day"), HTML.table(headings, past_day)
                ),
                TabPanel(
                    "Past week", HTML.h1("Past week"), HTML.table(headings, past_week)
                ),
                TabPanel(
                    "Past month",
                    HTML.h1("Past month"),
                    HTML.table(headings, past_month),
                ),
                TabPanel(
                    "Past year", HTML.h1("Past year"), HTML.table(headings, past_year)
                ),
            )
        )
