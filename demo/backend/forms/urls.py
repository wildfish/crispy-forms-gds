from django.urls import path
from django.views.generic import TemplateView

from .views import FormFieldView


app_name = "forms"

urlpatterns = [
    path(r"", TemplateView.as_view(template_name="forms/index.html"), name="index"),
    path(r"field/<str:field>/", FormFieldView.as_view(), name="field"),
]
