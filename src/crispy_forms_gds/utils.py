from django.conf import settings


def get_frontend_version():
    version = getattr(settings, "CRISPY_GDS_FRONTEND_VERSION", "5.0.0")
    return tuple(map(int, (version.split("."))))
