from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path(r"", RedirectView.as_view(url="forms"), name="home"),
    path(r"forms/", include("backend.forms.urls", namespace="forms")),
]
