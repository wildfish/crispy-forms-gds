from django.urls import path
from django.views.generic import TemplateView

from .views import ComponentView


app_name = "components"

urlpatterns = [
    path(r"", TemplateView.as_view(template_name="components/index.html"), name="index"),
    path(r"<str:name>/", ComponentView.as_view(), name="name"),
]
