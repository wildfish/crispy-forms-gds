from django.urls import include, path
from django.views.generic.base import TemplateView


urlpatterns = [
    path(r"", TemplateView.as_view(template_name="index.html"), name="home"),
    path(r"components/", include("backend.components.urls", namespace="components")),
]
