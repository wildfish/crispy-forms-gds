.. _Components: https://design-system.service.gov.uk/components
.. _Error summary: https://design-system.service.gov.uk/components/error-summary/

=======
Example
=======
You use crispy-forms-gds just like a regular crispy form. The minimum viable form
using this template pack is something like this: ::

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

All that is needed is to add the ``FormHelper`` class to the Form. Then in your
template add Design System `Error summary`_ and the ``crispy`` templatetag: ::

    {% load i18n crispy_forms_tags %}
    ...
    {% if form.helper.form_show_errors and form.errors %}
      {% include 'gds/layout/error_summary.html' %}
    {% endif %}
    ...
    {% crispy form %}
    ...

[That's way too much typing so if possible, we will look at replacing that conditional
with another templatetag, for example ``{% error_summary form %}``.]

The template pack takes care of all the rendering so the code above is displayed as:

.. image:: form.png

That's pretty basic but that's all you need to display forms that meet all the
requirements for presentation and accessibility, recommended and mandated by the
Design System guidelines.
