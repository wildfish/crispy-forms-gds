from django.urls import path

from .views import ComponentView, IndexView

app_name = "components"

urlpatterns = [
    path(r"", IndexView.as_view(), name="index"),
    path(r"<str:name>/", ComponentView.as_view(), name="name"),
]
