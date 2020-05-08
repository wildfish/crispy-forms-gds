.. _Checkboxes: https://design-system.service.gov.uk/components/checkboxes/

##########
Checkboxes
##########
To display a `Checkboxes`_ component you need to used a MultipleChoiceField with
the default widget, SelectMultiple replaced with a CheckboxSelectMultiple widget: ::

    from django import forms

    from crispy_forms_gds.helper import FormHelper
    from crispy_forms_gds.layout import Field, Layout, Size, Submit


    class CheckboxesForm(forms.Form):

        method = forms.MultipleChoiceField(
            choices=(("email", "Email"), ("phone", "Phone"), ("text", "Text message"),),
            widget=forms.CheckboxSelectMultiple,
            label="How would you like to be contacted?",
            help_text="Select all options that are relevant to you.",
            error_messages={"required": "Enter the ways to contact you"},
        )

        def __init__(self, *args, **kwargs):
            super(CheckboxesForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(
                Field.checkboxes(
                    "multiple",
                    legend_size=Size.MEDIUM,
                    hints={"phone": "Select this option only if you have a mobile phone"},
                ),
                Submit("submit", "Submit"),
            )

You can see this form live in the Demo site.

The set of checkboxes are wrapped in a <legend> with the field's label used as the
title. The keyword argument, ``legend_size`` is used to change the size and weight
of the font of the legend, otherwise the legend will be the same size as body text,
which is a bit unimposing. The ``Size`` class defines a set of string constants,
``SMALL``, ``MEDIUM``, ``LARGE`` and ``EXTRA_LARGE`` to make things a little more
readable but you can just use the corresponding values: ``'s'``, ``'m'``, ``'l'``
or ``'xl'`` directly if you prefer.

Im a multi-page form, where a single set of checkboxes is the only component on
a page, you can wrap the legend in an ``<h1>`` header tag by setting the ``legend_tag``
keyword argument to ``'h1'`` - leaving out the angle brackets. This avoids the duplication,
particularly for screen readers, of having a page title then the checkboxes' legend
effectively saying the same thing.

For each item in a set of checkboxes you can display an additional item of help
text in the form of a hint. The ``hints`` keyword argument takes a dictionary where
the keys are the respective checkbox value and the value is the hint to be displayed
below the checkbox label. That allows you to display hints as needed.

--------
Checkbox
--------
The Design System does not have an example showing a single checkbox. Presumably,
compared to a radio button with a Yes/No choice, a single checkbox, where the user
ticks the box if they agree with the question posed, is a poor user experience.

You can still, if so wish, add one to your form easily enough: ::

    from django import forms

    from crispy_forms_gds.helper import FormHelper
    from crispy_forms_gds.layout import Field, Layout, Submit


    class CheckboxesForm(forms.Form):

        single = forms.BooleanField(
            label="I accept the terms of service",
            help_text="Please read the terms of service and indicate whether you accept them.",
            error_messages={"required": "You must accept our terms of service"},
        )

        def __init__(self, *args, **kwargs):
            super(CheckboxesForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(
                Field.checkboxes("single", small=True),
                Submit("submit", "Submit"),
            )

The ``size`` keyword argument controls whether the size of the checkbox is
small, ``True`` or regular (largish), ``False``.
