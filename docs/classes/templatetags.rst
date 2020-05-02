=============
Template tags
=============

``{% crispy %}``
================

The crispy forms templatetag ``{% crispy form %}`` is still used to render
the form since the template pack is simply a plugin. ::

    {% load crispy_forms_tags crispy_forms_gds %}
    ...
    {% crispy form %}
    ...


``{% error_summary %}``
==========================

The Design System mandates that a summary of all the errors that occurred be
displayed at the top of the page, above the page heading. That is generally
outside the scope of the form. You could use the HTML layout classes to make
the page heading part of the form but that's somewhat ugly. Instead there is
a templatetag, ``{% error_summary %}`` that you can use to place the list
of errors exactly where you need it ::

    {% load crispy_forms_tags crispy_forms_gds %}
    ...
    {% error_summary form %}
    ...
    {% crispy form %}
    ...

If you choose not to display an error summary then you will need to set the
``show_non_field_errors`` on your ``FormHelper`` to True in order to get
non-field errors to be displayed, in the typical location, at the top of
your form: ::

        def __init__(self, *args, **kwargs):
            super(DateInputForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper(self)
            self.helper.show_non_field_errors = True


``{% crispy_gds_field %}``
==========================

.. automodule:: crispy_forms_gds.templatetags.crispy_forms_gds
   :members:
