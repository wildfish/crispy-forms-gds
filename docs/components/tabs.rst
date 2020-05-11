.. _Tabs: https://design-system.service.gov.uk/components/tabs/

####
Tabs
####
There are two Layout classes for adding `Tabs`_ component to a form: ``TabPanel``,
which contains the list of fields and other LayoutObjects which form the contents
of each panel and a parent ``Tabs`` which contains the list of panels. ::

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
                        "Past day",
                        HTML.h1("Past day"),
                        HTML.table(None, headings, past_day)
                    ),
                    TabPanel(
                        "Past week",
                        HTML.h1("Past week"),
                        HTML.table(None, headings, past_week)
                    ),
                    TabPanel(
                        "Past month",
                        HTML.h1("Past month"),
                        HTML.table(headings, past_month),
                    ),
                    TabPanel(
                        "Past year",
                        HTML.h1("Past year"),
                        HTML.table(None, headings, past_year)
                    ),
                )
            )

You can see this form live in the Demo site. Here we just copied the example
from the GOV.UK Design System site so all the layout objects are chunks of HTML.

The first argument passed to each ``TabPanel`` is the title, followed by the
list of fields or other layout objects that make up the contents. The ``Tabs``
object just contains the list of TabPanels.

When each tab is displayed the panel shrinks to fit the content. That's not a
a problem if the data is regular, as in the above example, or if the tabs are
displayed on a separate page in a multi-page form. It might not make for a good
visual experience if used on a large form however.

There is one complication. The name passed to the TabPanel is used to generate
the id attribute on the <div> that is used to create the panel. That means if
you have more than one set of tabs on a page with the same set of titles,
clicking on one panel brings to the front all the panels with the same name.
That is easily fixed however. Just set the ``css_id`` so you make the identifier
for each panel unique: ::

    HTML.h1("Past Week"),
    Tabs(
        TabPanel(
            "Opened", HTML.h1("Opened"), HTML.table(headings, past_week_opened)
        ),
        TabPanel(
            "Closed", HTML.h1("Closed"), HTML.table(headings, past_week_closed)
        )
    ),
    HTML.h1("Past Month"),
    Tabs(
        TabPanel(
            "Opened", HTML.h1("Opened"), HTML.table(headings, past_month_opened),
            css_id="past-month-opened"
        ),
        TabPanel(
            "Closed", HTML.h1("Closed"), HTML.table(headings, past_month_closed),
            css_id="past-month-closed"
        ),
    )

