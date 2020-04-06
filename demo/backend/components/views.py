from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from .forms import TextInputForm


class ComponentView(FormView):
    success_url = reverse_lazy("components:index")
    form_classes = {"text-input": TextInputForm}
    templates = {"text-input": "components/text_input.html"}

    def get_template_names(self):
        field_name = self.kwargs.get("field", "text-input")
        return [self.templates[field_name]]

    def get_form_class(self):
        field_name = self.kwargs.get("field", "text-input")
        return self.form_classes[field_name]
