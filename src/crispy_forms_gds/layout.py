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
    Used to create a button of any type::

        button = Button('Button 1', 'Press Me!')

    .. note:: The first argument is also slugified and turned into the id for the button.
    """

    template = "gds/layout/button.html"
    field_classes = "govuk-button"

    def __init__(self, name, value, **kwargs):
        super().__init__(name, value, **kwargs)
