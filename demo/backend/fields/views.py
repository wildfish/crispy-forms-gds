from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from .forms import (
    CompleteForm,
    ButtonsForm,
    CheckboxForm,
    CheckboxesForm,
    DetailsForm,
    FileUploadForm,
    InsetForm,
    PanelForm,
    RadiosForm,
    SelectForm,
    TagForm,
    TextareaForm,
    TextInputForm,
    WarningForm,
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
        "checkbox": CheckboxForm,
        "checkboxes": CheckboxesForm,
        "details": DetailsForm,
        "file-upload": FileUploadForm,
        "inset": InsetForm,
        "panel": PanelForm,
        "radios": RadiosForm,
        "select": SelectForm,
        "tag": TagForm,
        "text-input": TextInputForm,
        "textarea": TextareaForm,
        "warning": WarningForm,
    }
    contexts = {
        "buttons": {"title": "Buttons"},
        "checkbox": {"title": "Checkbox"},
        "checkboxes": {"title": "Checkboxes"},
        "details": {"title": "Details"},
        "file-upload": {"title": "File upload"},
        "inset": {"title": "Inset text"},
        "panel": {"title": "Panel"},
        "radios": {"title": "Radios"},
        "select": {"title": "Select"},
        "tag": {"title": "Tag"},
        "text-input": {"title": "Text input"},
        "textarea": {"title": "Textarea"},
        "warning": {"title": "Warning text"},
    }

    def get_form_class(self):
        field_name = self.kwargs["name"]
        return self.form_classes[field_name]

    def get_context_data(self, **kwargs):
        kwargs.update(self.contexts[self.kwargs["name"]])
        return super().get_context_data(**kwargs)
