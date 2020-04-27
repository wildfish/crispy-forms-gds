============
Templatetags
============

############
{% crispy %}
############
The crispy forms templatetag ``{% crispy form %}`` is still used to render
the form since the template pack is simply a plugin. ::

    {% load crispy_forms_tags %}
    ...
    {% if form.helper.form_show_errors and form.errors %}
      {% include 'gds/layout/error_summary.html' %}
    {% endif %}
    ...
    {% crispy form %}
    ...


######################
{% crispy_gds_field %}
######################

.. automodule:: crispy_forms_gds.templatetags.crispy_forms_gds_field
   :members:
