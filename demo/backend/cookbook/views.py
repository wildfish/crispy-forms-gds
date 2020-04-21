from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from .forms import CookbookForm


class IndexView(FormView):
    template_name = "cookbook/index.html"
    success_url = reverse_lazy("cookbook:index")
    form_class = CookbookForm
