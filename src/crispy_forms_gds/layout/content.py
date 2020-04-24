from crispy_forms import layout as crispy_forms_layout
from django.template import Context, Template
from django.utils.safestring import mark_safe


class Colour:
    """
    A set of constants for defining tag colours.
    """

    BLUE = "blue"
    GREEN = "green"
    GREY = "grey"
    ORANGE = "orange"
    PINK = "pink"
    PURPLE = "purple"
    RED = "red"
    TURQUOISE = "turquoise"
    YELLOW = "yellow"

    _values = (BLUE, GREEN, GREY, ORANGE, PINK, PURPLE, RED, TURQUOISE, YELLOW)

    @classmethod
    def is_valid(cls, value):
        return value in cls._values

    @classmethod
    def clean(cls, value):
        if not cls.is_valid(value):
            raise ValueError("Unexpected colour", value)
        return "govuk-tag--" + value


class HTML(crispy_forms_layout.HTML):
    @classmethod
    def details(cls, title, content):
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
        return HTML.heading("h1", "xl", content)

    @classmethod
    def h2(cls, content):
        return HTML.heading("h2", "l", content)

    @classmethod
    def h3(cls, content):
        return HTML.heading("h3", "m", content)

    @classmethod
    def h3(cls, content):
        return HTML.heading("h4", "s", content)

    @classmethod
    def inset(cls, content):
        snippet = '<div class="govuk-inset-text">%s</div>' % mark_safe(content)
        return HTML(snippet)

    @classmethod
    def p(cls, content):
        snippet = '<p class="govuk-body">%s</p>' % mark_safe(content)
        return HTML(snippet)

    @classmethod
    def panel(cls, title, content):
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
        snippet = '<strong class="govuk-tag %s">%s</strong>' % (
            Colour.clean(colour),
            mark_safe(title),
        )
        return HTML(snippet)

    @classmethod
    def warning(cls, content):
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
