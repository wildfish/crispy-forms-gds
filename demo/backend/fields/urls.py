from django.urls import path

from .views import FieldView, IndexView


app_name = "fields"

urlpatterns = [
    path(r"", IndexView.as_view(), name="index"),
    path(r"<str:name>/", FieldView.as_view(), name="name"),
]
