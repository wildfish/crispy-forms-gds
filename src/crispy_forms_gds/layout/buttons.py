from django.utils.text import slugify

import crispy_forms
from crispy_forms.layout import BaseInput


class Button(BaseInput):
    """
    Create a button of any type.

    Buttons are rendered by default as Design System primary buttons. When dealing with
    the basic objects you will need to pass the appropriate css class to get them to
    display as secondary or warning buttons.

    Examples: ::

        Button('add', 'Add contact')
        Button('cancel', 'Cancel', css_class="govuk-button--secondary")
        Button('delete', 'Delete account', css_class="govuk-button--warning")

    To save some typing there are class methods which save you the trouble of setting
    the css class: ::

        Button.primary('add', 'Add contact')
        Button.secondary('cancel', 'Cancel')
        Button.warning('delete', 'Delete account')

    Buttons are disabled by setting the disabled attribute to true: ::

        Button.primary('add', 'Add contact', disabled=True)

    Arguments:
        name (str): the value sent when the form is submitted.

        value (str): the button's title.

        disabled (bool, optional): is the button disabled. The default is ``False``.

        css_id (str, optional): an unique identifier for the <button>. Generally
            you will need to set this only if you need to add some javascript or
            very specific styling.

        css_class (str, optional): the names of one or more CSS classes that
            will be added to the <button>. The basic Design System CSS class,
            ``govuk-button`` is added automatically. This parameter is for any
            extra styling you want to apply.

        template (str, optional): the path to a template that overrides the
            one normally used.

        **kwargs: any additional attributes you want to add to the <button>.

    """

    template = "%s/layout/button.html"
    field_classes = "govuk-button"

    @classmethod
    def primary(cls, name, value, disabled=False, **kwargs):
        """Create a primary button."""
        return Button(name, value, disabled=disabled, **kwargs)

    @classmethod
    def secondary(cls, name, value, disabled=False, **kwargs):
        """Create a secondary button."""
        return Button(
            name,
            value,
            disabled=disabled,
            css_class="govuk-button--secondary",
            **kwargs,
        )

    @classmethod
    def warning(cls, name, value, disabled=False, **kwargs):
        """Create a warning button."""
        return Button(
            name, value, disabled=disabled, css_class="govuk-button--warning", **kwargs
        )

    def __init__(self, name, value, disabled=False, **kwargs):
        if disabled:
            kwargs["disabled"] = "disabled"
            kwargs["aria-disabled"] = "true"
        if not crispy_forms.__version__.startswith("1."):
            if "css_id" not in kwargs:
                kwargs["css_id"] = "id_%s" % slugify(name)
        super().__init__(name, value, data_module="govuk-button", **kwargs)


class Submit(BaseInput):
    """
    Create a Submit button.

    Submit buttons are rendered as ``input[type=submit]`` elements and work exactly
    the same way as primary Buttons. This is not a Design System component however
    it is included as it's a basic element of ``django-crispy-forms``.

    Examples: ::

        Submit('add', 'Add contact')
        Submit('add', 'Add contact', disabled=True)

    Args:
        name (str): the value sent when the form is submitted.

        value (str): the button's title.

        disabled (bool, optional): is the button disabled. The default is ``False``.

        css_id (str, optional): an unique identifier for the <input> element.
            Generally you will need to set this only if you need to add some
            javascript or very specific styling.

        css_class (str, optional): the names of one or more CSS classes that
            will be added to the <input> element. The basic Design System CSS class,
            ``govuk-button`` is added automatically. This parameter is for any
            extra styling you want to apply.

        template (str, optional): the path to a template that overrides the
            one normally used.

        **kwargs: any additional attributes you want to add to the <input>
            element.

    """

    input_type = "submit"
    field_classes = "govuk-button"
