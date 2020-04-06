from django.views.generic.edit import FormView
from django.urls import reverse_lazy


class PatternView(FormView):
    success_url = reverse_lazy("patterns:index")
    form_classes = {}
    templates = {}

    def get_template_names(self):
        field_name = self.kwargs["name"]
        return [self.templates[field_name]]

    def get_form_class(self):
        field_name = self.kwargs.get["name"]
        return self.form_classes[field_name]
