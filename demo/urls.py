from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.views.generic.base import TemplateView

urlpatterns = [
    path(r"", TemplateView.as_view(template_name="demo/index.html"), name="home"),
    path(r"components/", include("demo.components.urls", namespace="components")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
