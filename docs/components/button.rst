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

