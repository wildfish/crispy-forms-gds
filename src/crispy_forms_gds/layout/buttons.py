from crispy_forms.layout import BaseInput


class Submit(BaseInput):
    """
    Used to create a Submit button descriptor for the {% crispy %} template tag::

        submit = Submit('Search the Site', 'search this site')

    .. note:: The first argument is also slugified and turned into the id for the submit button.
    """

    input_type = "submit"
    field_classes = "govuk-button"


class Button(BaseInput):
    """
    Create a button of any type. ::

        button = Button('Button 1', 'Press Me!')
        button = Button('Button 1', 'Press Me!', css_class="govuk-button--secondary")
        button = Button('Button 1', 'Press Me!', disabled=True)

    Buttons are rendered by default as Design System primary buttons. You need to pass
    the css class to get them to display as secondary or warning buttons. To save some
    typing there are class methods which save you the trouble of setting the css class: ::

        button = Button.primary('Button 1', 'Press Me!')
        button = Button.secondary('Button 1', 'Press Me!')
        button = Button.warning('Button 1', 'Press Me!')

    """

    template = "gds/layout/button.html"
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
