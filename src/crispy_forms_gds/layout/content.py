from django.template import Context, Template
from django.utils.safestring import mark_safe

from crispy_forms import layout as crispy_forms_layout
from crispy_forms_gds.layout.constants import Colour


class HTML(crispy_forms_layout.HTML):
    """
    The HTML layout object lets you add general content to you form
    so you can avoid having to lay it out manually.

    You can pass in any string containing HTML: ::

        self.helper.layout = Layout(
            ...
            HTML("<p>This is the content for a paragraph.</p>"),
            ...
        )

    Alternatively, use one the class methods: ::

         self.helper.layout = Layout(
            ...
            HTML.p("This is the content for a paragraph."),
            ...
        )

    For something as simple a paragraph that does not save you much in
    typing. However where it really makes a difference is when layout
    complex things like tables which require a whole slew of classes to
    be added to the basic HTML: ::

        def __init__(self, *args, **kwargs):
            super(MyForm, self).__init__(*args, **kwargs)

            headings = ["Case manager", "Cases opened", "Cases closed"]

            data = [
                ["David Francis", "3", "0"],
                ["Paul Farmer", "1", "0"],
                ["Rita Patel", "2", "0"],
            ]

            self.helper = FormHelper()
            self.helper.layout = Layout(
                HTML.table(headings, data)
            )


    """

    @classmethod
    def details(cls, title, content):
        """
        .. _Details: https://design-system.service.gov.uk/components/details/

        Generate the layout for a `Details`_ component.

        Args:
            title: the text for the short link.
            content: the detailed description shown when the user clicks on the link.

        Returns:
            An HTML instance that can be added to a form's layout.

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

        Returns:
            An HTML instance that can be added to a form's layout.

        """
        return HTML.heading("h1", "xl", content)

    @classmethod
    def h2(cls, content):
        """
        Generate the HTML for a level two, ``<h2>``, heading.

        Args:
            content: the text for the heading.

        Returns:
            An HTML instance that can be added to a form's layout.

        """
        return HTML.heading("h2", "l", content)

    @classmethod
    def h3(cls, content):
        """
        Generate the HTML for a level three, ``<h4>``, heading.

        Args:
            content: the text for the heading.

        Returns:
            An HTML instance that can be added to a form's layout.

        """
        return HTML.heading("h3", "m", content)

    @classmethod
    def h4(cls, content):
        """
        Generate the HTML for a level four, ``<h4>``, heading.

        Args:
            content: the text for the heading.

        Returns:
            An HTML instance that can be added to a form's layout.

        """
        return HTML.heading("h4", "s", content)

    @classmethod
    def inset(cls, content):
        """
        .. _Inset text: https://design-system.service.gov.uk/components/inset-text/

        Generate the layout for an `Inset text`_ component.

        Args:
            content: the text to be displayed.

        Returns:
            An HTML instance that can be added to a form's layout.

        """
        snippet = '<div class="govuk-inset-text">%s</div>' % mark_safe(content)
        return HTML(snippet)

    @classmethod
    def p(cls, content):
        """
        Generate the HTML for a paragraph, ``<p>``.

        Args:
            content: the text to be displayed.

        Returns:
            An HTML instance that can be added to a form's layout.

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

        Returns:
            An HTML instance that can be added to a form's layout.

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
    def table(cls, headings, data):
        """
        .. _Table: https://design-system.service.gov.uk/components/table/

        Generate the layout for an `Table`_ component.

        Args:
            headings: the list of heading for the columns.
            data: the list of contents for each row - a list of lists of strings.

        Returns:
            An HTML instance that can be added to a form's layout.

        """
        context = Context(dict(headings=headings, data=data))
        template = """
            <table class="govuk-table">
            {% if headings %}
            <thead class="govuk-table__head">
              <tr class="govuk-table__row">
                {% for item in headings %}
                  <th scope="col" class="govuk-table__header">{{ item }}</th>
                {% endfor %}  
              </tr>
            </thead>
            {% endif %}
            <tbody class="govuk-table__body">
              {% for row in data %}
                <tr class="govuk-table__row">
                  {% for item in row %}
                    <td class="govuk-table__cell">{{ item }}</td>
                  {% endfor %}
                </tr>
              {% endfor %}
            </tbody>
            </table>
        """
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

        Returns:
            An HTML instance that can be added to a form's layout.

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

        Returns:
            An HTML instance that can be added to a form's layout.

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
