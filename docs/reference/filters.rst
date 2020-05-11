================
Template filters
================

The ``django-crispy-gds`` template pack includes a number of template filters.
These are all used internally when rendering the various components and will
definitely not be needed when rendering forms. They are included here for
reference in case you find something that might come in handy elsewhere.

There are also a set of filters in ``django-crispy-forms`` that are more generic
and might also be worth looking through.

is_checkbox
===========
Return ``True`` if the field is a (boolean) checkbox, ``False`` otherwise.

.. sourcecode:: html+django

    {% if field|is_checkbox %}


is_checkboxes
=============
Return ``True`` if the field belongs to a Checkboxes component, ``False`` otherwise.

.. sourcecode:: html+django

    {% if field|is_checkboxselectmultiple %}

This one is a bit of a nuisance to type so it will likely get deprecated and
replaced with ``is_checkboxes``.


is_file
=======
Return ``True`` if the field belongs to a File upload component, ``False`` otherwise.

.. sourcecode:: html+django

    {% if field|is_file %}


is_multivalue
=============
Return ``True`` if the field is a MultiValueField, ``False`` otherwise.

.. sourcecode:: html+django

    {% if field|is_multivalue %}


is_radios
=========
Return ``True`` if the field belongs to a Radios component, ``False`` otherwise.

.. sourcecode:: html+django

    {% if field|is_radioselect %}

