.. _Django: https://www.djangoproject.com/
.. _django-crispy-forms: https://github.com/maraujop/django-crispy-forms/
.. _GOV.UK Design System: https://design-system.service.gov.uk/
.. _Getting started: https://design-system.service.gov.uk/get-started/
.. _install guide: https://django-crispy-forms.readthedocs.io/en/latest/install.html
.. _production: https://design-system.service.gov.uk/get-started/production/
.. _webpack config: https://github.com/wildfish/crispy-forms-gds/blob/master/demo/frontend/webpack.config.js
.. _install nvm: https://github.com/nvm-sh/nvm

############
Introduction
############
This is a `Django`_ application to add `django-crispy-forms`_ template pack
and layout objects for the `GOV.UK Design System`_.

*******
Install
*******
This assumes you have already installed django-crispy-forms in your
project. If not, the `install guide`_ is very simple.

1. Install the package from PyPI: ::

    pip install crispy-forms-gds

2. Add the app to your settings: ::

    INSTALLED_APPS = (
        ...
        'crispy_forms_gds',
        ...
    )

3. Override the crispy_forms settings to set the template pack as the default: ::

    CRISPY_ALLOWED_TEMPLATE_PACKS = (
        "bootstrap", "bootstrap3", "bootstrap4", "uni_form", "gds"
    )
    CRISPY_TEMPLATE_PACK = "gds"

NOTE: The app does not include any GDS assets, you will have to install them
in your project. Details are provided on the `GOV.UK Design System`_ site.
Follow the `Getting started`_ guide and the installation instructions for a
`production`_ install. The demo site has a `webpack config`_ file which you
might find useful.

*******
Example
*******
To use the app just build a regular crispy form as before but the layout objects
are imported from crispy_forms_gds: ::

    from django import forms
    from django.utils.translation import ugettext_lazy as _

    from crispy_forms.helper import FormHelper
    from crispy_forms_gds.layout import Submit


    class TextInputForm(forms.Form):

        name = forms.CharField(
            label=_("Name"),
            widget=forms.TextInput(),
            help_text=_("Your full name."),
            error_messages={
                "required": _("Enter your name as it appears on your passport")
            }
        )

        def __init__(self, *args, **kwargs):
            super(TextInputForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.add_input(Submit("submit", _("Submit")))

And render the form in your templates: ::

    {% load i18n crispy_forms_tags %}
    ...
    {% crispy form %}
    ...

That's it.

****
Demo
****
If you checkout the code from the repository, there is a Django site you can run
to see the forms in action. You will need to `install nvm`_ for managing node
versions first. After that build everything and run the demo with: ::

    make serve

********
Requires
********
* Django >=2.2;
* django-crispy-forms >= 1.9.x;

*********
Resources
*********
.. _Read the docs: http://crispy-forms-gds.readthedocs.io/
.. _PyPi package: http://pypi.python.org/pypi/crispy-forms-gds
.. _Github repository: https://github.com/widlfish/crispy-forms-gds;
.. _Django Crispy Forms: https://django-crispy-forms.readthedocs.io/en/latest/

* Read the documentation on `Read the docs`_;
* Download the `PyPi package`_;
* Clone the `Github repository`_;
* Learn more about `Django Crispy Forms`_;
