from django.conf import settings


def frontend_version(request):
    return {"CRISPY_GDS_FRONTEND_VERSION": settings.CRISPY_GDS_FRONTEND_VERSION}
