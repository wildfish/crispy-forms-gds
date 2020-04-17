"""
MVS (Minimalist Viable Settings) for running the tests.

"""

INSTALLED_APPS = (
    "crispy_forms",
    "crispy_forms_gds",
)

ROOT_URLCONF = "tests.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {},
    },
]

CRISPY_ALLOWED_TEMPLATE_PACKS = ("gds",)

CRISPY_TEMPLATE_PACK = "gds"

CRISPY_FAIL_SILENTLY = False
