from django.urls import path
from django.views.generic import TemplateView

from .views import FieldView


app_name = "fields"

urlpatterns = [
    path(r"", TemplateView.as_view(template_name="fields/index.html"), name="index"),
    path(r"<str:name>/", FieldView.as_view(), name="name"),
]
