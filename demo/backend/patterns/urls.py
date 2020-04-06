from django.urls import path
from django.views.generic import TemplateView

from .views import PatternView


app_name = "patterns"

urlpatterns = [
    path(r"", TemplateView.as_view(template_name="patterns/index.html"), name="index"),
    path(r"<str:name>/", PatternView.as_view(), name="name"),
]
