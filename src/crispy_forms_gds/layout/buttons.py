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

    Buttons are disabled, in the usual way, by setting the disabled attribute to true: ::

        Button.primary('add', 'Add contact', disabled=True)

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
            **kwargs
        )

    @classmethod
    def warning(cls, name, value, disabled=False, **kwargs):
        """Create a warning button."""
        return Button(
            name, value, disabled=disabled, css_class="govuk-button--warning", **kwargs
        )

    def __init__(self, name, value, disabled=False, **kwargs):
        """
        Create a button.

        Args:
            name: the name of the button. This will be slugified when the button
                is rendered.

            value: the button title.

            disabled: is the button displayed initially disabled. Default is False.

            **kwargs: Attributes to add to the <button> element when it is rendered.

        """
        if disabled:
            kwargs["disabled"] = "disabled"
            kwargs["aria-disabled"] = "true"

        super().__init__(name, value, data_module="govuk-button", **kwargs)


class Submit(BaseInput):
    """
    Create a Submit button.

    Submit buttons are rendered as ``input[type=submit]`` elements and work exactly
    the same way as primary Buttons.

    As with Buttons, disabling a Submit button is simply a matter of setting the
    attribute.

    Examples: ::

        Submit('add', 'Add contact')
        Submit('add', 'Add contact', disabled=True)

    Args:
        name: the name of the button. This will be slugified when the button
            is rendered.

        value: the button title.

        **kwargs: Attributes to add to the <input> element when it is rendered.

    """

    input_type = "submit"
    field_classes = "govuk-button"
