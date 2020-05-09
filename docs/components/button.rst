.. _Button: https://design-system.service.gov.uk/components/button/

######
Button
######
A `Button`_ component is all you need to submit a form: ::

    from django import forms

    from crispy_forms_gds.helper import FormHelper
    from crispy_forms_gds.layout import Button, Layout, Div, Submit


    class ButtonsForm(forms.Form):

        name = forms.CharField(label="Your name")
        email = forms.CharField(label="Email")
        phone = forms.CharField(label="Phone")

        def __init__(self, *args, **kwargs):
            super(ButtonsForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(
                "name",
                "email",
                "phone",
                Submit("submit", "Add contact"))
            )

The first parameter is the value that will be submitted in the form and the second is
the button's title.

You don't need to use the ``Submit`` class which renders to an ``input[type=submit]``
element. Any ``<button>`` element within a ``<form>`` will trigger a submit when clicked: ::

        def __init__(self, *args, **kwargs):
            super(ButtonsForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(
                "name",
                "email",
                "phone",
                Button("submit", "Add contact"))
            )

``Submit`` and ``Button`` objects are displayed as primary buttons. The ``Button`` class
has a series of class methods that can be used to display the secondary and warning
buttons from the Design System: ::

    Button.primary("add", "Add contact")
    Button.secondary("find", "Find address")
    Button.warning("delete", "Delete account")

Disabling a button is simply a matter of adding the disabled attribute: ::

    Button.primary("win", "Win lottery", disabled=True)


Links
=====
You can also use the ``{% button_link %}`` template tag to style a link as a button::

    {% load crispy_forms_gds %}
    ...
    {% button_link url title %}

There is not a direct reference to styling links as button in the Design System guide,
apart from a "Start" button so we are not entirely sure this meets the criteria
especially for accessibility. However in our experience sometime a "Cancel" button is
needed (particularly in internal, not public facing sites) so hopefully this template
tag is useful.

Like any other template tag ``button_link`` can be used in a layout and so included in
a form::

    from crispy_forms_gds.templatetags.crispy_forms_gds import button_link

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML(button_link(reverse("home"), "Cancel")),
        )

Start button
------------
A Start button is just a button link with an inline icon. You use it the same way::

    {% load crispy_forms_gds %}
    ...
    {% button_start url 'Start now' %}

There is an example included on the Button component page in the Demo site.
