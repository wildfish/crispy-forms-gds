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


lookup
======
Looks up a value from a dict. Because Django still does not have this.

.. sourcecode:: html+django

    {{ dict|lookup:key }}

It's used when displaying the hint, if one is available for an item in
a list of checkboxes or radio buttons.

pop
===
Removes a value from a dict and displays it

.. sourcecode:: html+django

    {{ dict|pop:key }}

This is used when displaying the label for the individual fields in a
Date input component. The label was added as a widget attribute - it was
the only way to smuggle it in - and it needs to be remove from so it does
not get rendered as an attribute on the <input> element.
