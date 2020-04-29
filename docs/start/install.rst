.. _install-intro:

============
Installation
============

#.  Install ``django-crispy-forms`` using their `installation guide`__.

    .. __: https://django-crispy-forms.readthedocs.io/en/latest/install.html


#.  Install ``crispy-forms-gds`` from PyPI::

        pip install crispy-forms-gds


#.  Add the app to your settings::

        INSTALLED_APPS = (
            ...
            'crispy_forms_gds',
            ...

        )

#.  Override the crispy forms settings to set the template pack as the default::

        CRISPY_ALLOWED_TEMPLATE_PACKS = (
            "bootstrap", "bootstrap3", "bootstrap4", "uni_form", "gds"
        )
        CRISPY_TEMPLATE_PACK = "gds"


#.  Install the GDS assets using their `Getting started guide`_  and `production
    installation instructions`_.

    Our demo site has a `webpack config`_ file which you might find useful.

    .. _Getting started guide: https://design-system.service.gov.uk/get-started/
    .. _production installation instructions: https://design-system.service.gov.uk/get-started/production/
    .. _webpack config: https://github.com/wildfish/crispy-forms-gds/blob/master/demo/frontend/webpack.config.js
