from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from .forms import TextInputForm, CheckboxesForm


class FieldView(FormView):
    success_url = reverse_lazy("fields:index")
    form_classes = {
        "checkboxes": CheckboxesForm,
        "text-input": TextInputForm,
    }
    templates = {
        "checkboxes": "fields/checkboxes.html",
        "text-input": "fields/text-input.html",
    }

    def get_template_names(self):
        field_name = self.kwargs["name"]
        return [self.templates[field_name]]

    def get_form_class(self):
        field_name = self.kwargs["name"]
        return self.form_classes[field_name]
