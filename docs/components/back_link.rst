.. _Back link: https://design-system.service.gov.uk/components/back-link/

#########
Back link
#########
The `Back link`_ component is implemented as a template tag: ::

    {% load crispy_forms_gds %}
    ...
    <div class="govuk-width-container ">
      <main class="govuk-main-wrapper " id="main-content" role="main">

        {% url "home" as home_url %}
        {% back_link home_url %}
        ...

The title of the link defaults to "Back". If you need to change the title simply
pass it as an argument to the tag: ::

    {% back_link home_url "Take me back home" %}


There is an example of the ``{% back_link %}`` tag in the Demo site on the main
Components page.

You can also add the link to a form: ::

    from crispy_forms_gds.templatetags.crispy_forms_gds import back_link
    ...

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(
                HTML(back_link(reverse("home")))
            )

The Design System requires back links to be placed at the top of the page
above the title and the error summary so that pretty much rules adding the
back link in forms for pages that are public-facing.
