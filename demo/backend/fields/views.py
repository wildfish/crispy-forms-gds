from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from .forms import (
    CompleteForm,
    ButtonsForm,
    CheckboxesForm,
    FileUploadForm,
    RadiosForm,
    SelectForm,
    TextareaForm,
    TextInputForm,
)


class IndexView(FormView):
    template_name = "fields/index.html"
    success_url = reverse_lazy("fields:index")
    form_class = CompleteForm


class FieldView(FormView):
    template_name = "fields/field.html"
    success_url = reverse_lazy("fields:index")

    form_classes = {
        "buttons": ButtonsForm,
        "checkboxes": CheckboxesForm,
        "file-upload": FileUploadForm,
        "radios": RadiosForm,
        "select": SelectForm,
        "text-input": TextInputForm,
        "textarea": TextareaForm,
    }
    contexts = {
        "buttons": {"title": "Buttons"},
        "checkboxes": {"title": "Checkboxes"},
        "file-upload": {"title": "File upload"},
        "radios": {"title": "Radios"},
        "select": {"title": "Select"},
        "text-input": {"title": "Text input"},
        "textarea": {"title": "Textarea"},
    }

    def get_form_class(self):
        field_name = self.kwargs["name"]
        return self.form_classes[field_name]

    def get_context_data(self, **kwargs):
        kwargs.update(self.contexts[self.kwargs["name"]])
        return super().get_context_data(**kwargs)
