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
