.. _Breadcrumbs: https://design-system.service.gov.uk/components/breadcrumbs/

###########
Breadcrumbs
###########
The `Breadcrumbs`_ component is implemented as a inclusion tag: ::

    {% load crispy_forms_gds %}
    ...
    <div class="govuk-width-container ">
      <main class="govuk-main-wrapper " id="main-content" role="main">

        {% breadcrumbs links %}
        ...

The links argument is a list of 2-tuples. The first item is the title and
the second is the URL::

    links = [
        ("Home", reverse("home"),
        ("Components", reverse("components:index"),
        ("Breadcrumbs", None),
    ]

Only the title is displayed for the last item in the list, since it is (should be)
the current page. In this case you can simply set the URL to ``None``.

There is an example of the ``{% breadcrumbs %}`` tag in the Demo site at the top of
each page in the Components section. The list of links is created in the view that
renders those pages.

The ``{% breadcrumbs %}`` tag is an inclusion tag. if you wanted to add use it in
a form you would need to render the template snippet in your view and add it via
an ``HTML`` instance::

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        links = [
            ("Home", "/"),
            ("Previous", "/previous/"),
            ("Current", None),
        ]

        template = '{% include "gds/layout/breadcrumbs.html" %}'
        snippet = Template(template).render(Context(crumbs=links))

        self.helper.layout = Layout(
            HTML(snippet)
        )

The Design System requires breadcrumbs to be placed at the top of the page
above the title and the error summary. The same place as back links and so
outside the scope of the form. This is not going to work for public-facing
pages and generally it's less effort to simply pass the links in the context
and render them with the template tag.
