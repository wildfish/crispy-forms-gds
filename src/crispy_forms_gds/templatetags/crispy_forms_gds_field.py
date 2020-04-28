"""
This is a reimplementation of the crispy_forms_field template tag and
associated filters so the correct GDS classes can be added to input
elements. In particular the specific classes needed to render the
different input types and associated error classes when a validation
error is raised.

Examples:

    Rendering a field: ::

        {% load crispy_forms_gds_field %}
        ...
        {% crispy_gds_field field attrs %}

    Using the filters: ::

        {% if field|is_radioselect %}

Do not load the original crispy_forms_field at the same time as nothing
good will likely result.

The code was copied over verbatim from crispy_forms. Any additions are
clearly marked with a check to see if the 'gds' template pack is being
used.

The templatetag is only used within the gds/field.html template and you
probably won't have to deal with it, even if you are laying out a form
explicitly.

"""
from django import forms, template
from django.conf import settings

from crispy_forms.utils import TEMPLATE_PACK


register = template.Library()


@register.filter
def is_checkbox(field):
    """
    Template filter that returns True if the field is a checkbox, False otherwise.
    """
    return isinstance(field.field.widget, forms.CheckboxInput)


@register.filter
def is_password(field):
    """
    Template filter that returns True if the field is a password field,
    False otherwise.
    """
    return isinstance(field.field.widget, forms.PasswordInput)


@register.filter
def is_radioselect(field):
    """
    Template filter that returns True if the field is a set of radio
    buttons field, False otherwise.
    """
    return isinstance(field.field.widget, forms.RadioSelect)


@register.filter
def is_select(field):
    """
    Template filter that returns True if the field is a drop-down select
    field, False otherwise.
    """
    return isinstance(field.field.widget, forms.Select)


@register.filter
def is_checkboxselectmultiple(field):
    """
    Template filter that returns True if the field is set of checkboxes,
    False otherwise.
    """
    return isinstance(field.field.widget, forms.CheckboxSelectMultiple)


@register.filter
def is_file(field):
    """
    Template filter that returns True if the field is a file upload button,
    False otherwise.
    """
    return isinstance(field.field.widget, forms.FileInput)


@register.filter
def is_clearable_file(field):
    """
    Template filter that returns True if the field is a clearable file upload
    button, False otherwise.
    """
    return isinstance(field.field.widget, forms.ClearableFileInput)


@register.filter
def is_multivalue(field):
    """
    Template filter that returns True if the field is a multi-value field,
    False otherwise.
    """
    return isinstance(field.field.widget, forms.MultiWidget)


@register.filter
def classes(field):
    """
    Template filter that returns CSS classes of a field.
    """
    return field.widget.attrs.get("class", None)


@register.filter
def css_class(field):
    """
    Returns widget's class name in lowercase.
    """
    return field.field.widget.__class__.__name__.lower()


def pairwise(iterable):
    """
    Splits a list of items into pairs: s -> (s0,s1), (s2,s3), (s4, s5), ...
    """
    a = iter(iterable)
    return zip(a, a)


class CrispyGDSFieldNode(template.Node):
    """
    The TemplateNode used for rendering a field from the template pack.

    """

    def __init__(self, field, attrs):
        self.field = field
        self.attrs = attrs
        self.html5_required = "html5_required"

    def render(self, context):  # noqa: C901
        # Nodes are not threadsafe so we must store and look up our instance
        # variables in the current rendering context first
        if self not in context.render_context:
            context.render_context[self] = (
                template.Variable(self.field),
                self.attrs,
                template.Variable(self.html5_required),
            )

        field, attrs, html5_required = context.render_context[self]
        field = field.resolve(context)
        try:
            html5_required = html5_required.resolve(context)
        except template.VariableDoesNotExist:
            html5_required = False

        # If template pack has been overridden in FormHelper we can pick it from context
        template_pack = context.get("template_pack", TEMPLATE_PACK)

        # There are special django widgets that wrap actual widgets,
        # such as forms.widgets.MultiWidget, admin.widgets.RelatedFieldWidgetWrapper
        widgets = getattr(
            field.field.widget,
            "widgets",
            [getattr(field.field.widget, "widget", field.field.widget)],
        )

        if isinstance(attrs, dict):
            attrs = [attrs] * len(widgets)

        converters = {
            "checkboxinput": "govuk-checkboxes__input",
            "select": "govuk-select",
            "textinput": "govuk-input",
            "textarea": "govuk-textarea",
            "clearablefileinput": "govuk-file-upload",
        }
        converters.update(getattr(settings, "CRISPY_CLASS_CONVERTERS", {}))

        for widget, attr in zip(widgets, attrs):
            class_name = widget.__class__.__name__.lower()
            class_name = converters.get(class_name, class_name)

            if class_name:
                css_class = class_name.split()
            else:
                css_class = []

            for attr_css_class in widget.attrs.get("class", "").split():
                if attr_css_class not in css_class:
                    css_class.append(attr_css_class)

            css_class = " ".join(css_class)

            if (
                template_pack == "bootstrap3"
                and not is_checkbox(field)
                and not is_file(field)
                and not is_multivalue(field)
            ):
                css_class += " form-control"
                if field.errors:
                    css_class += " form-control-danger"

            if template_pack == "bootstrap4" and not is_multivalue(field):
                if not is_checkbox(field):
                    css_class += " form-control"
                    if is_file(field):
                        css_class += "-file"
                if field.errors:
                    css_class += " is-invalid"

            if template_pack == "gds":

                # The ability to override input_type was added to avoid having to create
                # new widgets. However, as a result, the browser validates the field and
                # displays a red border with no feedback to the user. That is at odds with
                # with the way the Design System reports errors. However this is being left
                # in for now until the "conflict" is better understood - it might be useful
                # to somebody at some point.

                if hasattr(widget, "input_type") and "input_type" in widget.attrs:
                    widget.input_type = widget.attrs.pop("input_type")

                if field.help_text:
                    widget.attrs["aria-describedby"] = "%s_hint" % field.auto_id

                if (
                    "class" in widget.attrs
                    and "govuk-js-character-count" in widget.attrs["class"]
                ):
                    if widget.attrs["aria-describedby"]:
                        widget.attrs["aria-describedby"] += " %s_info" % field.auto_id
                    else:
                        widget.attrs["aria-describedby"] = "%s_info" % field.auto_id

                if field.errors:

                    widget_class_name = widget.__class__.__name__

                    if widget_class_name in ["Select", "TextInput", "Textarea"]:
                        css_class += " govuk-input--error"
                    elif widget_class_name in ["FileInput", "ClearableFileInput"]:
                        css_class += " govuk-file-upload--error"

                    if not field.help_text:
                        widget.attrs["aria-describedby"] = ""

                    for idx, error in enumerate(field.errors, start=1):
                        css_error_class = "%s_%d_error" % (field.auto_id, idx)

                        if widget.attrs["aria-describedby"]:
                            widget.attrs["aria-describedby"] += " "

                        widget.attrs["aria-describedby"] += css_error_class

            widget.attrs["class"] = css_class

            # HTML5 required attribute
            if (
                html5_required
                and field.field.required
                and "required" not in widget.attrs
            ):
                if field.field.widget.__class__.__name__ != "RadioSelect":
                    widget.attrs["required"] = "required"

            for attribute_name, attribute in attr.items():
                attribute_name = template.Variable(attribute_name).resolve(context)

                if attribute_name in widget.attrs:
                    widget.attrs[attribute_name] += " " + template.Variable(
                        attribute
                    ).resolve(context)
                else:
                    widget.attrs[attribute_name] = template.Variable(attribute).resolve(
                        context
                    )

        return str(field)


@register.tag(name="crispy_gds_field")
def crispy_gds_field(parser, token):
    """
    The templatetag used to render fields from the template pack.

    Examples:

        ::

            {% crispy_gds_field field attrs %}
    """
    token = token.split_contents()
    field = token.pop(1)
    attrs = {}

    # We need to pop tag name, or pairwise would fail
    token.pop(0)
    for attribute_name, value in pairwise(token):
        attrs[attribute_name] = value

    return CrispyGDSFieldNode(field, attrs)
