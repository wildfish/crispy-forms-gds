.. _Select: https://design-system.service.gov.uk/components/select/

######
Select
######
Use a `Select`_ component only as a last resort for public facing services as there is
often a high rate of errors. ::

    from django import forms

    from crispy_forms_gds.helper import FormHelper


    class SelectForm(forms.Form):

        sort_by = forms.ChoiceField(
            choices=(
                ("published", "Recently published"),
                ("updated", "Recently updated"),
                ("views", "Most views"),
                ("comments", "Most comments"),
            ),
            widget=forms.Select,
            label="Sort by",
        )

        def __init__(self, *args, **kwargs):
            super(SelectForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()

You can see this form live in the Demo site.
