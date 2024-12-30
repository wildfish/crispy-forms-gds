from django.conf import settings


def gds_version(request):
    return {"GDS_VERSION": settings.GDS_VERSION}
