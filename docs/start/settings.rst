.. _django-crispy-forms: https://github.com/maraujop/django-crispy-forms
.. _GOV.UK Design System: https://design-system.service.gov.uk/

========
Settings
========

Crispy-forms-gds is a template pack so it only overrides settings from `django-crispy-forms`_ :

CRISPY_ALLOWED_TEMPLATE_PACKS
-----------------------------
Default: ("bootstrap", "uni_form", "bootstrap3", "bootstrap4")

This is the list of template packs supported by django-crispy-forms. You need
to add ``"gds"`` to the list otherwise an error will be raised: ::

    CRISPY_ALLOWED_TEMPLATE_PACKS = (
        "bootstrap", "uni_form", "bootstrap3", "bootstrap4", "gds"
    )

Since projects that are using the `GOV.UK Design System`_ are likely to have
a single style you can simply replace the list with: ::

    CRISPY_ALLOWED_TEMPLATE_PACKS = ("gds",)

CRISPY_TEMPLATE_PACK
--------------------
Default: "bootstrap"

This is the default template pack that will be used when rendering a form. Although
you can set the template pack on each individual form it's likely that when using
the `GOV.UK Design System`_ all forms will be rendered the same way. As a result, just
override this setting: ::

    CRISPY_TEMPLATE_PACK = "gds"

