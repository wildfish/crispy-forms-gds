from django.template import Context, Template
from django.utils.safestring import mark_safe

from crispy_forms import layout as crispy_forms_layout

from crispy_forms_gds.layout.constants import Colour


class HTML(crispy_forms_layout.HTML):
    """
    The HTML layout object lets you add general content to a form
    so you can avoid having to lay it out manually.

    You can pass in any string containing HTML::

        self.helper.layout = Layout(
            ...
            HTML("<p>This is the content for a paragraph.</p>"),
            ...
        )

    Arguments:
        html (str): the unescaped HTML to be displayed.

    To make life easier there are several class methods which generate
    various HTML elements::

        HTML.p("This is the content for a paragraph.")

    For something as simple a paragraph that does not save you much in
    typing. However where it really makes a difference is when layout
    complex things like a Details component which require a whole slew
    of classes to be added to the basic HTML. Compare::

        HTML.details(
            "Help with nationality",
            "We need to know your nationality so we can work out which "
            "elections you’re entitled to vote in.",
        )

    to the actual layout::

        HTML('<details class="govuk-details" data-module="govuk-details">
              <summary class="govuk-details__summary">
                <span class="govuk-details__summary-text">Help with nationality</span>
              </summary>
              <div class="govuk-details__text">
                  We need to know your nationality so we can work out which
                  elections you’re entitled to vote in.
              </div>
            </details>')

    The set of class methods is not comprehensive. For now, only the most common
    HTML elements and Design System components are included. More will added as
    the need and demand arises.

    """

    @classmethod
    def details(cls, title, content):
        """
        .. _Details: https://design-system.service.gov.uk/components/details/

        Generate the layout for a `Details`_ component.

        Args:
            title: the text for the short link.
            content: the detailed description shown when the user clicks on the link.

        """
        snippet = """
            <details class="govuk-details" data-module="govuk-details">
              <summary class="govuk-details__summary">
                <span class="govuk-details__summary-text">%s</span>
              </summary>
              <div class="govuk-details__text">%s</div>
            </details>
            """ % (
            mark_safe(title),
            mark_safe(content),
        )
        return HTML(snippet)

    @classmethod
    def heading(cls, tag, size, content):
        snippet = '<{0} class="govuk-heading-{1}">{2}</{0}>'.format(tag, size, content)
        return HTML(snippet)

    @classmethod
    def h1(cls, content):
        """
        Generate the HTML for a level one, ``<h1>``, heading.

        Args:
            content: the text for the heading.

        """
        return HTML.heading("h1", "xl", content)

    @classmethod
    def h2(cls, content):
        """
        Generate the HTML for a level two, ``<h2>``, heading.

        Args:
            content: the text for the heading.

        """
        return HTML.heading("h2", "l", content)

    @classmethod
    def h3(cls, content):
        """
        Generate the HTML for a level three, ``<h4>``, heading.

        Args:
            content: the text for the heading.

        """
        return HTML.heading("h3", "m", content)

    @classmethod
    def h4(cls, content):
        """
        Generate the HTML for a level four, ``<h4>``, heading.

        Args:
            content: the text for the heading.

        """
        return HTML.heading("h4", "s", content)

    @classmethod
    def inset(cls, content):
        """
        .. _Inset text: https://design-system.service.gov.uk/components/inset-text/

        Generate the layout for an `Inset text`_ component.

        Args:
            content: the text to be displayed.

        """
        snippet = '<div class="govuk-inset-text">%s</div>' % mark_safe(content)
        return HTML(snippet)

    @classmethod
    def p(cls, content):
        """
        Generate the HTML for a paragraph, ``<p>``.

        Args:
            content: the text to be displayed.

        """
        snippet = '<p class="govuk-body">%s</p>' % mark_safe(content)
        return HTML(snippet)

    @classmethod
    def panel(cls, title, content):
        """
        .. _Panel: https://design-system.service.gov.uk/components/panel/

        Generate the layout for an `Panel`_ component.

        Args:
            title: the title.
            content: the message (subtitle).

        """
        snippet = """
            <div class="govuk-panel govuk-panel--confirmation">
              <h1 class="govuk-panel__title">%s</h1>
              <div class="govuk-panel__body">%s</div>
            </div>
            """ % (
            mark_safe(title),
            mark_safe(content),
        )
        return HTML(snippet)

    @classmethod
    def table(cls, headers, rows, caption=None, header_css=None, row_css=None):
        """
        .. _Table: https://design-system.service.gov.uk/components/table/

        Generate the layout for an `Table`_ component.

        Eaxample: ::

            caption = "Dates and amounts"
            headers = ["Date", "Amount"]

            header_css = [
                "govuk-!width-one-half",
                "govuk-table__header--numeric govuk-!width-one-half"
            ]

            rows = [
                ["First six weeks (per week)", "£109.80"]
                ["Next 33 weeks (per week)", "£109.80"]
                [Total estimated pay", "£4,282.20"]
            ]

            row_css = ["". "govuk-table__cell--numeric"]

            self.helper.layout = Layout(
                HTML.table(headers, rows, caption, header_css, row_css)
            )


        Args:
            headers: the list of heading for the columns.

            rows: a two dimensional list containing the data for each cell.

            caption (str, optional): a caption describing the table.

            header_css (list): css classes that are added to each column in the header.

            row_css (list): css classes that are added to each column in each row

        """
        if headers is None:
            headers = []

        if not header_css:
            header_css = [""] * len(headers)

        if not row_css and rows:
            row_css = [""] * len(rows[0])

        headers = zip(headers, header_css)
        rows = [zip(row, row_css) for row in rows]

        context = Context(dict(caption=caption, headers=headers, rows=rows))
        template = """
            <table class="govuk-table">
            {% if caption %}
              <caption class="govuk-table__caption">{{ caption }}</caption>
            {% endif %}
            {% if headers %}
            <thead class="govuk-table__head">
              <tr class="govuk-table__row">
                {% for col in headers %}
                  <th scope="col" class="govuk-table__header{% if col.1 %} {{ col.1 }}{% endif %}">{{ col.0 }}</th>
                {% endfor %}
              </tr>
            </thead>
            {% endif %}
            <tbody class="govuk-table__body">
              {% for row in rows %}
                <tr class="govuk-table__row">
                  {% for col in row %}
                    <td class="govuk-table__cell{% if col.1 %} {{ col.1 }}{% endif %}">{{ col.0 }}</td>
                  {% endfor %}
                </tr>
              {% endfor %}
            </tbody>
            </table>
        """  # noqa
        return HTML(Template(template).render(context))

    @classmethod
    def tag(cls, title, colour):
        """
        .. _Tag: https://design-system.service.gov.uk/components/tag/

        Generate the layout for an `Tag`_ component.

        NOTE: the name of the colour is not validated so this method can still
        be used if the Design System adds new colours not supported by the
        template pack.

        Args:
            title: the text that is displayed in the tag.
            colour: the name of the background colour used in the tag.

        """
        snippet = '<strong class="govuk-tag %s">%s</strong>' % (
            Colour.for_tag(colour, validate=False),
            mark_safe(title),
        )
        return HTML(snippet)

    @classmethod
    def warning(cls, content):
        """
        .. _Warning text: https://design-system.service.gov.uk/components/warning-text/

        Generate the layout for an `Warning text`_ component.

        Args:
            content: the message that is displayed as a warning.

        """
        snippet = """
            <div class="govuk-warning-text">
              <span class="govuk-warning-text__icon" aria-hidden="true">!</span>
              <strong class="govuk-warning-text__text">
                <span class="govuk-warning-text__assistive">Warning</span>
                %s
              </strong>
            </div>
        """ % (
            mark_safe(content),
        )
        return HTML(snippet)
