from crispy_forms import helper as crispy_forms_helper
from crispy_forms.utils import TEMPLATE_PACK

from crispy_forms_gds.layout import Size


class FormHelper(crispy_forms_helper.FormHelper):
    """
    .. _FormHelper: https://django-crispy-forms.readthedocs.io/en/latest/form_helper.html  # noqa

    This class controls the form rendering behavior of the form passed to
    the ``{% crispy %}`` tag. It intended to be use exclusively with the 'gds'
    template pack and extends the django-crispy-forms FormHelper class by
    adding the following attributes to control how the form is rendered.

    Attributes:
        show_non_field_errors (bool): display non-field errors at the top of
            the form. The default is ``False`` as the Design System mandates
            that all form errors are displayed in an Error Summary at the top
            of the page (above the page title and outside the <form>). Only
            set this to ``True`` if you are not using an Error Summary.

        label_size (:obj:`str`, optional): set the default size used for all
            field labels. The default value of None renders labels with the
            same font size as body text. To change the font size and weight
            use one of the pre-defined Design System sizes: 's', 'm', 'l'
            or 'xl'.

        legend_size (:obj:`str`, optional): set the default size used for
            fields that use <legend> instead of <label> (checkboxes and radios).
            The default value of None renders labels with the same font size
            as body text. To change the font size and weight use one of the
            pre-defined Design System sizes: 's', 'm', 'l' or 'xl'.

    These attributes are added as template variables. They can be overridden
    on each field, as required.

    Examples:

        You use FormHelper the same way as the django-crispy-form version.

        Let the FormHelper create a default layout for the form: ::

            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.helper = FormHelper(self)

        Create a custom Layout: ::

            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.helper = FormHelper()
                self.helper.layout = Layout(
                   ...
                )

    All the existing `FormHelper`_ methods are available if you need something
    specific.

    """

    show_non_field_errors = False
    label_size = ""
    legend_size = ""

    def render_layout(self, form, context, template_pack=TEMPLATE_PACK):
        """
        Returns safe html of the rendering of the layout.

        :meta private:
        """
        # Django will add a required attribute when a field is rendered, if is
        # required by the form. The browser validation interferes with the way
        # validation errors are reported so adding required attributes is
        # disabled at the form level.
        form.use_required_attribute = False

        if self.label_size:
            context["label_size"] = Size.for_label(self.label_size)
        if self.legend_size:
            context["legend_size"] = Size.for_legend(self.legend_size)

        return super().render_layout(form, context, template_pack=template_pack)
