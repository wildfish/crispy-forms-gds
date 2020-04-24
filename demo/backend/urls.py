from django.urls import include, path
from django.views.generic.base import RedirectView


urlpatterns = [
    path(r"", RedirectView.as_view(url="components/"), name="home"),
    path(r"components/", include("backend.components.urls", namespace="components")),
]
