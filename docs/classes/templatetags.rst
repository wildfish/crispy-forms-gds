============
Templatetags
============

############
{% crispy %}
############
The crispy forms templatetag ``{% crispy form %}`` is still used to render
the form since the template pack is simply a plugin. ::

    {% load crispy_forms_tags crispy_forms_gds_tags %}
    ...
    {% error_summary form %}
    ...
    {% crispy form %}
    ...


######################
{% crispy_gds_field %}
######################

.. automodule:: crispy_forms_gds.templatetags.crispy_forms_gds_field
   :members:
