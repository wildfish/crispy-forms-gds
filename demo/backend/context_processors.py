from django.conf import settings


def tutorial(request):
    return {"HAS_TUTORIAL_APP": "backend.tutorial" in settings.INSTALLED_APPS}
