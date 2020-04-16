from crispy_forms import helper as crispy_forms_helper
from crispy_forms.utils import TEMPLATE_PACK


class FormHelper(crispy_forms_helper.FormHelper):
    """
    This class controls the form rendering behavior of the form passed to
    the `{% crispy %}` tag. It intended to be use exclusively with the 'gds'
    template pack and adds the following attributes to control how the form
    is rendered:

        **form_show_error_summary**: Display a Design System Error Summary
            containing field  and non-field errors at the top of the form. An
            error summary is displayed by default.

        **form_show_required_attribute**: Control whether a required attribute
            is displayed when a widget is rendered. The default is not to show
            the attribute as it triggers the browser to interfere with the way
            field errors are shown.

    """

    form_show_error_summary = True
    form_show_required_attribute = False

    def render_layout(self, form, context, template_pack=TEMPLATE_PACK):
        """
        Returns safe html of the rendering of the layout
        """
        form.use_required_attribute = self.form_show_required_attribute
        return super().render_layout(form, context, template_pack=template_pack)
