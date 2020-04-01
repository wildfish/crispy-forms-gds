# Introduction
This is a [Django](https://www.djangoproject.com/) application to add 
[django-crispy-forms](https://github.com/maraujop/django-crispy-forms/) template pack
and layout objects for the [GOV.UK Design System](https://design-system.service.gov.uk/).

## Install
This assumes you have already installed `django-crispy-forms`_ in your
project. If not, the `install guide`_ is very simple.

1. Install the package from PyPI:
    ```shell script
    pip install crispy-forms-gds
    ```
2. Add the app to your settings:
    ```
    INSTALLED_APPS = (
       ...
       'crispy_forms_gds',
       ...
    )
    ```
3. Override the crispy_forms settings to set the template pack as the default:
    ```
    CRISPY_ALLOWED_TEMPLATE_PACKS = (
        "bootstrap", "bootstrap3", "bootstrap4", "uni_form", "gds"
    )
    CRISPY_TEMPLATE_PACK = "gds"
    ```

NOTE: The app does not include any GDS assets, you will have to install them 
in your project. Details are provided on the 
[GOV.UK Design System](https://design-system.service.gov.uk/) 
site. Follow the [GOV.UK Design System](https://design-system.service.gov.uk/get-started/) 
guide and the installation instructions for a
[GOV.UK Design System](https://design-system.service.gov.uk/get-started/production/) install.

## Use
To use the app just build a regular crispy form as before but the layout objects 
are imported from `crispy_forms_gds`:

```python
from django import forms
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms_gds.layout import Submit


class TextInputForm(forms.Form):

    name = forms.CharField(
        label=_("Name"),
        widget=forms.TextInput(attrs={"width": 9}),
        help_text=_("Your full name."),
        error_messages={
            "required": _("Enter your name as it appears on your passport")
        }
    )

    def __init__(self, *args, **kwargs):
        super(TextInputForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", _("Submit")))
```
And render the form in your templates:
```djangotemplate
{% load i18n crispy_forms_tags %}
...
{% crispy form %}
...
```
That's it.

You may have noticed the ``width`` attribute on the ``TextInput`` widget. You
can use this to set 
[appropriately sized text widths](https://design-system.service.gov.uk/components/text-input/#use-appropriately-sized-text-inputs)
on the field when the form is is rendered. Crispy-forms-gds makes it easy to set 
GDS-specific styles without having to add the class names - though you can to that 
too. Check out the description for each element in the ``User Reference`` section
of the docs.

## Requires
* Django >=2.2;
* django-crispy-forms >= 1.9.x;

## Resources
* Read the documentation on [Read the docs](http://crispy-forms-gds.readthedocs.io/);
* Download the [PyPi package](http://pypi.python.org/pypi/crispy-forms-gds);
* Clone the [Github repository](https://github.com/widlfish/crispy-forms-gds);
* Learn more about [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/);
