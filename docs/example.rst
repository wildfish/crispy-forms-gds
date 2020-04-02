.. _appropriately sized text widths: https://design-system.service.gov.uk/components/text-input/#use-appropriately-sized-text-inputs

=======
Example
=======
You use crispy-forms-gds just like a regular crispy form except you import
the layout objects from ``crispy_forms_gds.layout`` since these have the GDS
specific classes added: ::

    from django import forms
    from django.utils.translation import ugettext_lazy as _

    from crispy_forms.helper import FormHelper
    from crispy_forms_gds.layout import Submit


    class FormidableForm(forms.Form):

        name = forms.CharField(
            label=_("Name"),
            widget=forms.TextInput(),
            help_text=_("Your full name."),
            error_messages={
                "required": _("Enter your name as it appears on your passport")
            }
        )

        def __init__(self, *args, **kwargs):
            super(TextInputForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.add_input(Submit("submit", _("Submit")))

Then you render the form in true, crispy style: ::

    {% load i18n crispy_forms_tags %}
    ...
    {% crispy form %}
    ...

That's it.
