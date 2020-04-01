.. _django-crispy-forms: https://github.com/maraujop/django-crispy-forms
.. _install guide: https://django-crispy-forms.readthedocs.io/en/latest/install.html
.. _GOV.UK Design System: https://design-system.service.gov.uk/
.. _Getting started: https://design-system.service.gov.uk/get-started/
.. _production: https://design-system.service.gov.uk/get-started/production/

.. _install-intro:

=======
Install
=======
This guide assumes you have already installed `django-crispy-forms`_ in your
project. If not, the `install guide`_ is very simple.

#. Install the package from PyPI: ::

    pip install crispy-forms-gds

#. Add the apps to your settings: ::

        INSTALLED_APPS = (
           ...
           'crispy_forms_gds',
           ...
        )

#. Update the crispy_forms settings to activate the template pack: ::

        CRISPY_ALLOWED_TEMPLATE_PACKS = (
            "bootstrap", "uni_form", "bootstrap3", "bootstrap4", "gds"
        )
        CRISPY_TEMPLATE_PACK = "gds"

NOTE: The app does not include any GDS assets, you will have to install them
in your projects. Details are provided on the `GOV.UK Design System`_ site.
Follow the `Getting Started`_ guide and the installation instructions for a
`production`_ install.
