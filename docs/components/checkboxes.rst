.. _Checkboxes: https://design-system.service.gov.uk/components/checkboxes/

##########
Checkboxes
##########
A `Checkboxes`_ component is used to render multiple ChoiceField and BooleanField
though you need to override the default widget used by Django on the form. ::

    from django import forms

    from crispy_forms_gds.helper import FormHelper
    from crispy_forms_gds.layout import Field, Layout, Size, Submit


    class CheckboxesForm(forms.Form):

        multiple = forms.ChoiceField(
            choices=(("email", "Email"), ("phone", "Phone"), ("text", "Text message"),),
            widget=forms.CheckboxSelectMultiple,
            label="How would you like to be contacted?",
            help_text="Select all options that are relevant to you.",
            error_messages={"required": "Enter the ways to contact you"},
        )

        single = forms.BooleanField(
            label="I accept the terms of service",
            help_text="Please read the terms of service and indicate whether you accept them.",
            error_messages={"required": "You must accept our terms of service"},
        )

        def __init__(self, *args, **kwargs):
            super(CheckboxesForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(
                Field.checkbox("multiple", legend_size=Size.MEDIUM), "single"
            )
            self.helper.add_input(Submit("submit", "Submit"))

You can see this form live in the Demo site.
