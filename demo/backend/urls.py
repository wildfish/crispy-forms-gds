from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path(r"", RedirectView.as_view(url="fields/"), name="home"),
    path(r"fields/", include("backend.fields.urls", namespace="fields")),
]
