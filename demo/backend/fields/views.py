from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from .forms import CheckboxesForm, RadiosForm, SelectForm, TextareaForm, TextInputForm


class FieldView(FormView):
    success_url = reverse_lazy("fields:index")
    form_classes = {
        "checkboxes": CheckboxesForm,
        "radios": RadiosForm,
        "select": SelectForm,
        "text-input": TextInputForm,
        "textarea": TextareaForm,
    }
    templates = {
        "checkboxes": "fields/checkboxes.html",
        "radios": "fields/radios.html",
        "select": "fields/select.html",
        "text-input": "fields/text-input.html",
        "textarea": "fields/textarea.html",
    }

    def get_template_names(self):
        field_name = self.kwargs["name"]
        return [self.templates[field_name]]

    def get_form_class(self):
        field_name = self.kwargs["name"]
        return self.form_classes[field_name]
