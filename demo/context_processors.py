from crispy_forms_gds.utils import get_frontend_version


def frontend_version(request):
    return {"CRISPY_GDS_FRONTEND_VERSION": get_frontend_version()}
