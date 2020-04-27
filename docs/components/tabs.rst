.. _Tabs: https://design-system.service.gov.uk/components/tabs/

####
Tabs
####
There are two Layout classes for adding an `Tabs`_ to a form. ``TabPanel``
which wraps the contents of each section and ``Tabs`` which wraps the sections
and adds the ability to step between them. ::

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

You can see this form live in the Demo site.

The first argument passed to the ``TabPanel`` is the title, followed by the
list of fields or other layout objects that will shown in the section. Here
we just copied the example from the GOV.UK Design System site so all the
layout objects are chunks of HTML.

When each tab is displayed the panel shrinks to fit the content. That's not a
a problem if the data is regular, as in the above example, or if the tabs are
displayed on a separate page in a multi-page form. It might not make for a good
visual experience if used on a large form however.
