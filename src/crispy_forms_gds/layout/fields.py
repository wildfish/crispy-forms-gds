from django.template.loader import render_to_string
from django.utils.html import conditional_escape

from crispy_forms import layout as crispy_forms_layout
from crispy_forms.utils import TEMPLATE_PACK, flatatt
from crispy_forms_gds.layout import Fixed, Fluid, Size


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
    def checkboxes(
        cls, field, legend_size=None, legend_tag=None, small=False, hints=None, **kwargs
    ):
        """
        Create a field for displaying checkboxes.

        Args:
            field (str): the name of the field.

            legend_size (str): the size of the legend. The default is None in which
                case the legend will be rendered at the same size as regular text.

            legend_tag (str): Wrap the field legend with this HTML tag.
                Default is None.

            small (bool): Display small checkboxes. Default is False.

            hints (dict): Hints that will be displayed for one or more checkboxes.
                The dictionary key is the checkbox value. Defaults to None.

            **kwargs: Attributes to add to the <input> element when the field is
                rendered.

        Returns:
            a Field object configured to display a Checkboxes component.

        """
        context = {}

        if legend_size:
            context["legend_size"] = Size.for_legend(legend_size)

        if legend_tag:
            context["legend_tag"] = legend_tag

        context["checkboxes_small"] = small

        if hints:
            context["checkboxes_hints"] = hints

        return Field(field, context=context, **kwargs)

    @classmethod
    def radios(
        cls,
        field,
        legend_size=None,
        legend_tag=None,
        small=False,
        inline=False,
        hints=None,
        **kwargs
    ):
        """
        Create a field for displaying radio buttons.

        Args:
            field (str): the name of the field.

            legend_size (str): the size of the legend. The default is None in which
                case the legend will be rendered at the same size as regular text.

            legend_tag (str): Wrap the field legend with this HTML tag.
                Default is None.

            small (bool): Display small radio buttons. Default is False.

            inline (bool): Display the radio buttons in a row. Default is False.

            hints (dict): Hints that will be displayed for one or more checkboxes.
                The dictionary key is the checkbox value. Defaults to None.

            **kwargs: Attributes to add to the <input> element when the field is
                rendered.

        Returns:
            a Field object configured to display a Radios component.

        """
        context = {}

        if legend_size:
            context["legend_size"] = Size.for_legend(legend_size)

        if legend_tag:
            context["legend_tag"] = legend_tag

        context["radios_small"] = small
        context["radios_inline"] = inline

        if hints:
            context["radios_hints"] = hints

        return Field(field, context=context, **kwargs)

    @classmethod
    def select(cls, field, legend_size=None, legend_tag=None, **kwargs):
        """
        Create a field for displaying a select drop-down.

        Args:
            field (str): the name of the field.

            legend_size (str): the size of the legend. The default is None in which
                case the legend will be rendered at the same size as regular text.

            legend_tag (str): Wrap the field legend with this HTML tag.
                Default is None.

            **kwargs: Attributes to add to the <select> element when the field is
                rendered.

        Returns:
            a Field object configured to display a Select component.

        """
        context = {}

        if legend_size:
            context["legend_size"] = Size.for_legend(legend_size)

        if legend_tag:
            context["legend_tag"] = legend_tag

        return Field(field, context=context, **kwargs)

    @classmethod
    def text(cls, field, label_size=None, label_tag=None, field_width=None, **kwargs):
        """
        Create a field for displaying a Text input.

        Args:
            field (str): the name of the field.

            label_size (str): the size of the label. The default is None in which
                case the label will be rendered at the same size as regular text.

            label_tag (str): Wrap the field label with this HTML tag.
                Default is None.

            field_width (int, str): the width of the field - fixed or fluid. The
                default is None in which case the field will be rendered full width.

            **kwargs: Attributes to add to the <input> element when the field is
                rendered.

        Returns:
            a Field object configured to display a Text input.

        """
        context = {}

        if label_size:
            context["label_size"] = Size.for_label(label_size)

        if label_tag:
            context["label_tag"] = label_tag

        if field_width:
            if isinstance(field_width, int):
                css_class = Fixed.for_input(field_width)
            else:
                css_class = Fluid.for_input(field_width)
        else:
            css_class = kwargs.get("css_class")

        return Field(field, css_class=css_class, context=context, **kwargs)

    @classmethod
    def textarea(
        cls,
        field,
        label_size=None,
        label_tag=None,
        rows=10,
        max_characters=None,
        max_words=None,
        threshold=None,
        **kwargs
    ):
        """
        Create a field for displaying a Textarea.

        Args:
            field (str): the name of the field.

            label_size (str): the size of the label. The default is None in which
                case the label will be rendered at the same size as regular text.

            label_tag (str): Wrap the field label with this HTML tag.
                Default is None.

            rows (int): the number of rows to display. If not specified then Django's
                default of 10 will be used (the default used by most browsers is 2).

            max_characters (int, optional): the maximum number of characters that should be entered.
                Default is None.

            max_words (int, optional): the maximum number of words that should be entered.
                Default is None.

            threshold (int, optional): the percentage of the count that has to be reached
                before the limit is shown. Default is None.

            **kwargs: Attributes to add to the <textarea> element when the field is
                rendered.

        Raises:
            ValueError: if you set max_characters and max_words at the same time.

        Returns:
            a Field object configured to display a Text input.

        """
        context = {}

        if label_size:
            context["label_size"] = Size.for_label(label_size)

        if label_tag:
            context["label_tag"] = label_tag

        kwargs["rows"] = rows

        if max_characters and max_words:
            raise ValueError(
                "Cannot set max_characters and max_words at the same time."
            )

        if threshold and not max_characters and not max_words:
            raise ValueError(
                "Cannot set the typing threshold without setting the maximum "
                "number of characters of words."
            )

        if max_characters:
            context["max_characters"] = max_characters

        if max_words:
            context["max_words"] = max_words

        if max_characters or max_words:
            kwargs["css_class"] = "govuk-js-character-count"

            if threshold:
                context["threshold"] = threshold

        return Field(field, context=context, **kwargs)

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

            Field('name', context={'label_tag': 'h1', 'label_size': 'govuk-label--xl'})
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

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK, **kwargs):
        template = self.get_template_name(template_pack)
        return self.get_rendered_fields(
            form,
            form_style,
            context,
            template_pack,
            template=template,
            attrs=self.attrs,
            extra_context=self.context,
            **kwargs,
        )


class Hidden(crispy_forms_layout.Hidden):
    pass
