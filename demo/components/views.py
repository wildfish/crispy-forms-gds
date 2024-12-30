from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import (
    AccordionForm,
    ButtonsForm,
    CheckboxesForm,
    ConditionalRadiosForm,
    DateInputForm,
    DetailsForm,
    FieldsetForm,
    FileUploadForm,
    InsetForm,
    PanelForm,
    RadiosForm,
    SelectForm,
    TabsForm,
    TagForm,
    TextareaForm,
    TextInputForm,
    WarningForm,
)


class IndexView(TemplateView):
    template_name = "components/index.html"


class ComponentView(FormView):
    template_name = "components/component.html"
    success_url = reverse_lazy("components:index")

    form_classes = {
        "accordion": AccordionForm,
        "buttons": ButtonsForm,
        "checkboxes": CheckboxesForm,
        "conditional_radios": ConditionalRadiosForm,
        "date-input": DateInputForm,
        "details": DetailsForm,
        "fieldset": FieldsetForm,
        "file-upload": FileUploadForm,
        "inset": InsetForm,
        "panel": PanelForm,
        "radios": RadiosForm,
        "select": SelectForm,
        "tabs": TabsForm,
        "tag": TagForm,
        "text-input": TextInputForm,
        "textarea": TextareaForm,
        "warning": WarningForm,
    }
    contexts = {
        "accordion": {"title": "Accordion"},
        "buttons": {"title": "Buttons"},
        "checkboxes": {"title": "Checkboxes"},
        "conditional_radios": {"title": "Conditional Radios"},
        "date-input": {"title": "Date input"},
        "details": {"title": "Details"},
        "fieldset": {"title": "Fieldset"},
        "file-upload": {"title": "File upload"},
        "inset": {"title": "Inset text"},
        "panel": {"title": "Panel"},
        "radios": {"title": "Radios"},
        "select": {"title": "Select"},
        "tabs": {"title": "Tabs"},
        "tag": {"title": "Tag"},
        "text-input": {"title": "Text input"},
        "textarea": {"title": "Textarea"},
        "warning": {"title": "Warning text"},
    }

    def get_form_class(self):
        component_name = self.kwargs["name"]
        return self.form_classes[component_name]

    def get_context_data(self, **kwargs):
        kwargs.update(self.contexts[self.kwargs["name"]])
        kwargs["breadcrumbs"] = (
            ("Home", reverse("home")),
            ("Components", reverse("components:index")),
            (kwargs["title"], None),
        )
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        if "continue" in form.data:
            return super().form_invalid(form)
        else:
            form.valid_layout()
            return super().form_invalid(form)
