=======
Example
=======

Use ``crispy-forms-gds`` like a normal crispy form::

    from django import forms

    from crispy_forms_gds.helper import FormHelper
    from crispy_forms_gds.layout import Submit


    class MinimumForm(forms.Form):

        name = forms.CharField(
            label="Name",
            help_text="Your full name.",
            error_messages={
                "required": "Enter your name as it appears on your passport"
            }
        )

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper(self)
            self.helper.add_input(Submit("submit", _("Submit")))


Add the ``FormHelper`` class to the form, then in your template add the
``error_summary`` template tag to display the Design System `Error summary`_. Use the
``crispy`` template tag to display the form as normal::

    {% load i18n crispy_forms_tags crispy_forms_gds_tags %}
    ...
    {% error_summary form %}
    ...
    {% crispy form %}
    ...

.. _Error summary: https://design-system.service.gov.uk/components/error-summary/


The template pack takes care of all the rendering so the code above is displayed as:

.. image:: form.png

This will display forms that meet all the requirements for presentation and
accessibility, recommended and mandated by the Design System guidelines.
