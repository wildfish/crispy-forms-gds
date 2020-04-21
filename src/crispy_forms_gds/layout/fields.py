from django.utils.html import conditional_escape

from crispy_forms import layout as crispy_forms_layout
from crispy_forms.utils import TEMPLATE_PACK


class Size:
    """
    A set of constants for setting the size of labels, legends or headings.
    """

    SMALL = "s"
    MEDIUM = "m"
    LARGE = "l"
    EXTRA_LARGE = "xl"

    _values = (SMALL, MEDIUM, LARGE, EXTRA_LARGE)

    @classmethod
    def is_valid(cls, value):
        return value in cls._values

    @classmethod
    def clean(cls, value):
        if not cls.is_valid(value):
            raise ValueError("Unexpected size", value)
        return value


class Fixed:
    """
    A set of constants for setting a fixed width on Text inputs.
    """

    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    TEN = 10
    TWENTY = 20
    THIRTY = 30

    _values = (TWO, THREE, FOUR, FIVE, TEN, TWENTY, THIRTY)

    @classmethod
    def is_valid(cls, value):
        return value in cls._values

    @classmethod
    def clean(cls, value):
        if not cls.is_valid(value):
            raise ValueError("Unexpected fixed width", value)
        return "govuk-input--width-%d" % value


class Fluid:
    """
    A set of constants for setting a fluid width on Text inputs.
    """

    ONE_QUARTER = "one-quarter"
    ONE_THIRD = "one-third"
    ONE_HALF = "one-half"
    TWO_THIRDS = "two-thirds"
    THREE_QUARTERS = "three-quarters"
    FULL = "full"

    _values = (
        ONE_QUARTER,
        ONE_THIRD,
        ONE_HALF,
        TWO_THIRDS,
        THREE_QUARTERS,
        FULL,
    )

    @classmethod
    def is_valid(cls, value):
        return value in cls._values

    @classmethod
    def clean(cls, value):
        if not cls.is_valid(value):
            raise ValueError("Unexpected fluid width", value)
        return "govuk-!-width-%s" % value


class Field(crispy_forms_layout.LayoutObject):
    """
    A Layout object for display one or more fields in a form.

    Field instances are rather low level, however, they give you better control
    over setting the css classes and HTML attributes on a field. You can also
    set template variables to control the rendering of all the markup - labels
    etc. that make up a field.

    For general use it's simpler to use the class methods to generate Field
    instances. This hide some of the details in the way the field is rendered
    and give more of a "component" feel. You can always update the instances
    after  if you need to.

    Examples::

        Field.text("name", label_size=Size.MEDIUM, field_width=Fluid.ONE_HALF)

    Field is a copy of the Crispy Forms Field class but with more well-defined
    interface. The ability to set template variables was added and the template
    keyword argument was made explicit - before it was just another kwarg. The
    one incompatibility is the wrapper_class keyword argument, which was removed.
    You can still add it via the context since it was used as a template variable.
    """

    template = "%s/field.html"

    @classmethod
    def text(
        cls, field, label_size=None, label_is_heading=False, field_width=None, **kwargs
    ):
        """
        Create a field for displaying a Text input.

        Args:
            field (str): the name of the field.

            label_size (str): the size of the label. The default is None in which
                case the label will be rendered at the same size as regular text.

            label_is_heading (bool): Use the field label as the page title.
                Default is False.

            field_width (int, str): the width of the field - fixed or fluid. The
                default is None in which case the field will be rendered full width.

            **kwargs: Attributes to add to the <input> element when the field is
                rendered.

        Returns:
            a Field object configured to display a Text input.

        """
        css_class = None
        context = {}

        if label_size:
            context["field_label_size"] = Size.clean(label_size)

        if label_is_heading:
            context["field_label_is_heading"] = True

        if field_width:
            if isinstance(field_width, int):
                css_class = Fixed.clean(field_width)
            else:
                css_class = Fluid.clean(field_width)

        return Field(field, css_class=css_class, context=context, **kwargs)

    def __init__(self, *fields, css_class=None, context=None, template=None, **kwargs):
        """
        Create a Field for adding to a Layout.

        Args:
            *fields: the names of the fields to display.

            css_class (str): the css classes that will be added to the widget.

            context (dict): the list of values that will be added to the template
                context when the field is rendered.

            template (str): the template used to render this field, overriding the
                one defined on the class.

            **kwargs (str): the list of attributes that will be added to the widget. Use '_'
                instead of '-' in the attribute name. It will be converted to '-'.

        The variables defined in the context are only in scope while the field is
        being rendered. The original template context is then restored.

        Examples::

            Field('name', context={'field_label_is_heading': True, 'field_label_size': 'govuk-label--xl'})
            Field('age', css_class="govuk-input-width-5", style="color: #333;")

        """
        self.fields = list(fields)

        if hasattr(self, "attrs"):
            self.attrs = self.attrs.copy()
        else:
            self.attrs = {}

        if hasattr(self, "context"):
            self.context = self.context.copy()
        else:
            self.context = {}

        if css_class:
            self.add_class(css_class)

        if context:
            self.context.update(context)

        if template:
            self.template = template

        self.add_attributes(**kwargs)

    def add_field(self, field):
        """
        Add a field to the list that will be rendered.

        Generally a Field is only used to render one form field. Multiple
        fields are only used when you want to render them in the same way.
        The most likely case is when displays the list of fields for a
        street address. The fields are rendered in the order they are added
        to the Field.

        Args:
            field: the name of the form field.

        """
        self.fields.append(field)

    def add_class(self, css_class):
        """
        Add a CSS class to the field.

        Args:
            css_class (str): the CSS class name.

        """
        if "class" in self.attrs:
            self.attrs["class"] += " " + css_class
        else:
            self.attrs["class"] = css_class

    def add_context(self, **kwargs):
        """
        Add values to the context used when rendering the field.

        The scope of the values is limited to the rendering of the field. After
        that the original template context will be restored.

        Args:
            **kwargs: keyword arguments that will be added as template variables.

        Returns:

        """
        self.context.update(kwargs)

    def add_attributes(self, **kwargs):
        """
        Add one or more HTML attributes to the field.

        Underscores in names are converted to hyphens, e.g. data_id='test' is converted
        to data-id='test'.

        Args:
            **kwargs: keyword arguments that will be added as HTML attributes.

        Returns:

        """
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
