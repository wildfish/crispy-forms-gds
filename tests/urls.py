from django.urls import path
from django.views.generic import View


urlpatterns = [
    path("", View.as_view(), name="home"),
]
