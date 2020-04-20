from django.utils.html import conditional_escape

from crispy_forms import layout as crispy_forms_layout
from crispy_forms.utils import TEMPLATE_PACK


class Field(crispy_forms_layout.LayoutObject):
    """
    Layout object used to control how a form field is rendered.

    Args:
        *fields: the names of the fields to display.

        css_class (str): the css classes that will be added to the widget.

        context (dict): the list of values that will be added to the template
            context when the field is rendered.

        **kwargs (str): the list of attributes that will be added to the widget. Use '_'
            instead of '-' in the attribute name. It will be converted to '-'.

    The variables defined in the extra context are only in scope while the field is
    being rendered. The original template context is then restored.

    Some default values are defined on the FormHelper. These will be applied to every
    field unless overridden here. For example, setting field labels to be displayed
    in a bold font rather than the default styling. Other variables only make sense
    to define on a field-by-field basis. For example, using the label of the first
    field as the page heading, by setting `field_label_is_heading` to True.

    https://design-system.service.gov.uk/get-started/labels-legends-headings/

    Examples::

        Field('name', context={'field_label_is_heading': True, 'field_label_size': 'xl'})
        Field('age', css_class="govuk-input-width-5", style="color: #333;")

    """

    template = "%s/field.html"

    @classmethod
    def _create_field(cls, *fields, css_class=None, context=None, **kwargs):
        if css_class:
            kwargs["css_class"] = css_class
        if context:
            kwargs["context"] = context
        return Field(*fields, **kwargs)

    @classmethod
    def fullname(cls, *fields, css_class=None, context=None, **kwargs):
        """
        Create a Field that can be used for a person's complete name.
        """
        attrs = {"autocomplete": "name", "spellcheck": "false"}
        attrs.update(kwargs)
        return cls._create_field(*fields, css_class=css_class, context=context, **attrs)

    @classmethod
    def email(cls, *fields, css_class=None, context=None, **kwargs):
        """
        Create a Field that can be used for an email address.
        """
        attrs = {"autocomplete": "email", "spellcheck": "false"}
        attrs.update(kwargs)
        return cls._create_field(*fields, css_class=css_class, context=context, **attrs)

    @classmethod
    def number(cls, *fields, css_class=None, context=None, **kwargs):
        """
        Create a Field that can be used for entering a number.
        """
        attrs = {"inputmode": "numeric", "pattern": "[0-9]*"}
        attrs.update(kwargs)
        return cls._create_field(*fields, css_class=css_class, context=context, **attrs)

    def __init__(self, *fields, css_class=None, context=None, **kwargs):
        self.fields = list(fields)

        if not hasattr(self, "attrs"):
            self.attrs = {}
        else:
            # Make sure shared state is not edited.
            self.attrs = self.attrs.copy()

        if not hasattr(self, "context"):
            self.context = {}
        else:
            self.context = self.context.copy()

        if css_class:
            if "class" in self.attrs:
                self.attrs["class"] += " %s" % css_class
            else:
                self.attrs["class"] = css_class

        if context:
            self.context.update(context)

        self.context["wrapper_class"] = kwargs.pop("wrapper_class", None)

        self.template = kwargs.pop("template", self.template)

        if "extra" in kwargs:
            self.extra.update(kwargs.pop("extra"))

        # We use kwargs as HTML attributes, turning data_id='test' into data-id='test'
        self.attrs.update(
            {k.replace("_", "-"): conditional_escape(v) for k, v in kwargs.items()}
        )

    def render(
        self,
        form,
        form_style,
        context,
        template_pack=TEMPLATE_PACK,
        extra_context=None,
        **kwargs
    ):
        if extra_context is None:
            extra_context = {}

        extra_context.update(self.context)

        template = self.get_template_name(template_pack)

        return self.get_rendered_fields(
            form,
            form_style,
            context,
            template_pack,
            template=template,
            attrs=self.attrs,
            extra_context=extra_context,
            **kwargs,
        )


class Hidden(crispy_forms_layout.Hidden):
    pass
