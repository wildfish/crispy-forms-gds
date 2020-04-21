from django import forms
from django.utils.translation import ugettext_lazy as _

from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import Button, Field, Layout


class CompleteForm(forms.Form):

    text_input = forms.CharField(label=_("Text input"), required=False,)

    textarea = forms.CharField(
        label=_("Textarea"), widget=forms.Textarea, required=False,
    )

    upload = forms.FileField(label=_("File upload"), required=False,)

    radios = forms.ChoiceField(
        label=_("Radios"),
        choices=(("yes", _("Yes")), ("no", _("No")),),
        widget=forms.RadioSelect,
        required=False,
    )

    select = forms.ChoiceField(
        label=_("Select"),
        choices=(
            ("", _("Choose")),
            ("published", _("Recently published")),
            ("updated", _("Recently updated")),
            ("views", _("Most views")),
            ("comments", _("Most comments")),
        ),
        widget=forms.Select,
        required=False,
    )

    checkboxes = forms.ChoiceField(
        label=_("Checkboxes"),
        choices=(
            ("email", _("Email")),
            ("phone", _("Phone")),
            ("text", _("Text message")),
        ),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.field_label_size = "m"
        self.helper.layout = Layout(
            Field("text_input", css_class="govuk-!-width-one-half"),
            Field("textarea", rows="3"),
            Field("upload"),
            Field("radios"),
            Field("select"),
            Field("checkboxes"),
            Button(
                "continue",
                _("Continue"),
                css_class="govuk-!-margin-right-3",
                data_module="govuk-button",
            ),
            Button(
                "cancel",
                _("Cancel"),
                css_class="govuk-button--secondary",
                data_module="govuk-button",
            ),
        )
