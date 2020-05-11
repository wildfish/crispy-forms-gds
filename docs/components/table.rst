.. _Table: https://design-system.service.gov.uk/components/table/

#####
Table
#####
A `Table`_ component is implemented using the ``HTML.table()`` class method
to generate the HTML object that can be added to a form::

    def __init__(self, *args, **kwargs):
        super(TabsForm, self).__init__(*args, **kwargs)

        caption = "This week"
        headers = ["Case manager", "Cases opened", "Cases closed"]
        rows = [
            ["David Francis", "24", "18"],
            ["Paul Farmer", "16", "20"],
            ["Rita Patel", "24", "27"],
        ]
        header_css = [
            "govuk-!-width-one-half",
            "govuk-table__header--numeric",
            "govuk-table__header--numeric",
        ]
        row_css = [
            "",
            "govuk-table__cell--numeric",
            "govuk-table__cell--numeric"
        ]

        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML.table(caption, headers, rows, header_css, row_css)
        )

The method is simple to use but rather basic. The caption and the header are
optional. Set them to ``None`` if not needed. The number of columns in the
header and each row should match - you cannot leave entries out if the contents
are blank.

The Design System CSS classes needed to style the table are added
by default. You can add additional classes to set the column widths or alignment
by passing one or more CSS classes as a string in the ``header_css`` or ``row_css``
arguments.

The method works perfectly well for small amounts of data, particularly on
public-facing pages where the intent is just data presentation. For more
sophisticated uses where the volume of data is large and splitting the table
across pages or being able to sort data in columns is needed then consider
looking at a package such `django-tables2`_.

.. _django-tables2: https://django-tables2.readthedocs.io/en/latest/


