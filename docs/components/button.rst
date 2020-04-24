.. _Buttons: https://design-system.service.gov.uk/components/button/

======
Button
======
A `Button`_ component is all you need to submit a form: ::

    from django import forms

    from crispy_forms_gds.helper import FormHelper
    from crispy_forms_gds.layout import Button, Layout, Div, Submit


    class ButtonsForm(forms.Form):
        def __init__(self, *args, **kwargs):
            super(ButtonsForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(
                Div(Button.primary("continue", "Save and continue")),
                Div(Button.secondary("find", "Find address")),
                Div(Button.primary("win", "Win lottery", disabled=True)),
                Div(Button.warning("delete", "Delete account")),
                Div(Submit('submit', "Submit"))
            )

You can see this form live in the Demo site.

Any ``<button>`` element within a ``<form>`` will trigger a submit when clicked.
So you don't need to use the ``Submit`` class which renders to an ``input[type=submit]``
element.

Incidentally, the buttons here are wrapped in a ``Div`` purely to add some spacing
between them. You don't need to do this in real life.
