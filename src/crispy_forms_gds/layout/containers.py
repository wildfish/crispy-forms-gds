from django.template.loader import render_to_string
from django.utils.text import slugify

from crispy_forms import layout as crispy_forms_layout
from crispy_forms.utils import TEMPLATE_PACK, flatatt, render_field
from crispy_forms_gds.layout import Size


class Div(crispy_forms_layout.Div):
    """
    A layout object for displaying a Div.

    Div is just a general-purpose container for laying out forms. It
    inherits everything from it's ``django-crispy-forms`` parent. it is
    include in the template pack as it make imports easier.

    Although there is the Fieldset component for grouping fields together
    a Div is quite useful when you just need to add some spacing between
    elements.

    Examples: ::

        Div("name", "email", "phone", css_class="govuk-!-margin-bottom-5")
        Button.primary("add", "Add contact")

    Args:
        *fields: a list of ``LayoutObjects`` - fields, buttons, HTML,
            etc. that displayed inside the <div> element.

        **kwargs: the keyword arguments supported by a ``LayoutObject``:
            ``css_id`` - the unique identifier for the component;
            ``css_class`` - additional css classes that can be used to
            style the <div> and ``template`` - the path to another
            template that can be used to render the accordion. The
            remaining keyword arguments are added as attributes to the
            <div> element.

     """

    pass


class Accordion(Div):
    """
    .. _Accordion: https://design-system.service.gov.uk/components/accordion/

    A layout object for displaying an `Accordion`_ component.

    Accordion is the parent object to which you add an ``AccordionSection`` for
    each of the panels you want to display.

    Each accordion on a given page must have a unique identifier so the
    javascript controls that open and close the panels can be added by
    the Design System. The default value is 'accordion' so you don't
    need to set it if there is only one.

    Examples: ::

        Accordion(
            AccordionSection("group name", "form_field_1", "form_field_2"),
            AccordionSection("another group name", "form_field")
        )

        Accordion(
            AccordionSection("group name", "form_field_1", "form_field_2"),
            css_id="accordion-1"
        )

    Args:
        *fields: a list of AccordionSection objects that are the panels
            that make up this accordion.

        **kwargs: the keyword arguments supported by a ``LayoutObject``:
            ``css_id`` - the unique identifier for the component;
            ``css_class`` - additional css classes that can be used to
            style the accordion and ``template`` - the path to another
            template that can be used to render the accordion. The
            remaining keyword arguments are added as attributes to the
            parent <div> that is to create the accordion.

    """

    template = "%s/accordion.html"

    def __init__(self, *fields, **kwargs):
        super().__init__(*fields, **kwargs)
        if not self.css_id:
            self.css_id = "accordion"

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK, **kwargs):
        content = ""
        for index, group in enumerate(self.fields, start=1):
            context["index"] = index
            context["parent"] = self.css_id
            content += render_field(
                group, form, form_style, context, template_pack=template_pack, **kwargs
            )
        template = self.get_template_name(template_pack)
        context.update({"accordion": self, "content": content})
        return render_to_string(template, context.flatten())


class AccordionSection(Div):
    """
    .. _Accordion: https://design-system.service.gov.uk/components/accordion/

    A layout object for displaying a panel in an `Accordion`_ component.

    The AccordionSection has a title and an optional summary that describes
    the contents of the panel. The contents can be one or more LayoutObjects:
    fields, buttons, composed layouts, etc. You cannot nest Accordions however.
    (The controls don't work - all the panels are open. It's visually confusing
    as the styling assumes only one level).

    Examples: ::

        AccordionSection("title", "form_field_1", "form_field_2")

        AccordionSection(
            "title",
            "form_field_1",
            summary="A short description of the contents"
        )

    Args:
        name (str): the title of the panel.

        summary (str, optional): a short description of the panel contents.

        *fields: a list of LayoutObjects objects that make up the panel contents.

        **kwargs: the keyword arguments supported by a ``LayoutObject``:
            ``css_id`` - the unique identifier for the component;
            ``css_class`` - additional css classes that can be used to
            style the accordion section and ``template`` - the path to
            another template that can be used to render the section. The
            remaining keyword arguments are added as attributes to the
            <div> that is to create the section.

    """

    template = "%s/accordion-group.html"
    css_class = ""

    def __init__(self, name, *fields, summary=None, **kwargs):
        super().__init__(*fields, **kwargs)
        self.name = name
        self.summary = summary
        self.index = None
        self.parent = None

    def __contains__(self, field_name):
        """
        check if field_name is contained within tab.
        """
        return field_name in map(lambda pointer: pointer[1], self.get_field_names())

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK, **kwargs):
        self.index = context.get("index", None)
        self.parent = context.get("parent")
        return super().render(form, form_style, context, template_pack)


class Fieldset(crispy_forms_layout.LayoutObject):
    """
    A layout object for displaying groups of fields.

    The contents of a Fieldset are be one or more LayoutObjects: fields, buttons,
    composed layouts, etc.

    A Fieldset has an optional title which is created using a <legend> element.
    The title size is set from one of the predefined Design System sizes:
    small ('s'), medium ('m'), large ('l') or extra-large ('xl'). The sizes are
    defined as constants on the ``Size`` class. The size is translated to the
    appropriate CSS class when the Fieldset is rendered. If the Fieldset is the
    only element on the page you can "promote" the <legend> to become the page
    title by wrapping it in an <h1> tag. The avoids the duplication that would
    result, particularly for screen readers, where the page had both a title and
    the Fieldset <legend>.

    Examples: ::

        Fieldset('form_field_1', 'form_field_2')
        Fieldset('form_field_1', 'form_field_2', legend="fieldset_title")
        Fieldset('form_field_1', 'form_field_2', legend="fieldset_title", legend_tag="h1")
        Fieldset('form_field_1', 'form_field_2', legend="fieldset_title", legend_size="xl")

    Args:
        legend (str, optional): the title displayed in a <legend>.
        legend_size (str, optional): the size of the title: 's', 'm', 'l' or
            'xl'.
        legend_tag (str, optional): an HTML tag that wraps the <legend>. Normally
            this is 'h1' so the <legend> also acts as the page title.

        *fields: a list of LayoutObjects objects that make up the Fieldset contents.

        **kwargs: the keyword arguments supported by a ``LayoutObject``:
            ``css_id`` - the unique identifier for the component;
            ``css_class`` - additional css classes that can be used to style
            the <fieldset> and ``template`` - the path to another template
            that can be used to render the <fieldset>. The remaining keyword
            arguments are added as attributes to the <fieldset> element.

   """

    css_class = "govuk-fieldset"
    template = "%s/layout/fieldset.html"

    def __init__(
        self, *fields, legend=None, legend_size=None, legend_tag=None, **kwargs
    ):
        self.fields = list(fields)
        self.context = {}

        if legend:
            self.context["legend"] = legend

        if legend_size:
            self.context["legend_size"] = Size.for_legend(legend_size)

        if legend_tag:
            self.context["legend_tag"] = legend_tag

        if hasattr(self, "css_class") and "css_class" in kwargs:
            self.css_class += " %s" % kwargs.pop("css_class")
        if not hasattr(self, "css_class"):
            self.css_class = kwargs.pop("css_class", None)

        self.css_id = kwargs.pop("css_id", None)
        self.template = kwargs.pop("template", self.template)
        self.flat_attrs = flatatt(kwargs)

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK, **kwargs):
        fields = self.get_rendered_fields(
            form, form_style, context, template_pack, **kwargs
        )
        context = {
            "fieldset": self,
            "fields": fields,
            "form_style": form_style,
        }
        context.update(self.context)
        template = self.get_template_name(template_pack)
        return render_to_string(template, context)


class Tabs(Div):
    """
    A layout object for displaying a set of tabs.

    ``Tabs`` contains a list of ``TabPanels`` which in turn contains the
    list of fields and other layout objects which make up the content of
    each tab.

    Example: ::

        Tabs(
            TabPane('tab_name_1', 'form_field_1', 'form_field_2'),
            TabPane('tab_name_2', 'form_field_3')
        )

    Args:
        *fields: a list of TabPanel objects that make up the set of tabs.

        **kwargs: the keyword arguments supported by a ``LayoutObject``:
            ``css_id`` - the unique identifier for the component;
            ``css_class`` - additional css classes that can be used to style
            the parent <div> and ``template`` - the path to another template
            that can be used to render the set of tabs. The remaining keyword
            arguments are added as attributes to the parent <div> element.

    The ``css_id`` keyword argument generally is not needed since the javascript
    added by the Design System applies to the daughter ``TabPanels`` and not the
    parent <div>.

    """

    template = "%s/layout/tabs.html"

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK, **kwargs):
        content = self.get_rendered_fields(form, form_style, context, template_pack)
        links = "".join(tab.render_link(template_pack) for tab in self.fields)
        context.update({"tabs": self, "links": links, "content": content})
        template = self.get_template_name(template_pack)
        return render_to_string(template, context.flatten())


class TabPanel(Div):
    """
    A layout object that displays the contents of each pane in a set of tabs.

    The contents of a ``TabPanel`` can be any set of Fields, HTML content,
    LayoutObject or composed layout. You cannot nest sets of tabs. It works
    visually, although the appearance is a little cluttered, however the
    javascript that controls the switching between tabs does not work.

    Example::

        TabPanel('tab_name', 'form_field_1', 'form_field_2', 'form_field_3')

    Args:
        name (str): the title of the panel. This is also used as the id
            for the <div> that displays the contents.

        *fields: a list of layout objects that make up the contents of the panel.

        **kwargs: the keyword arguments supported by a ``LayoutObject``:
            ``css_id`` - the unique identifier for the component;
            ``css_class`` - additional css classes that can be used to style
            the parent <div> of the panel and ``template`` - the path to another
            template that can be used to render the set of tabs. The remaining
            keyword arguments are added as attributes to the parent <div> element.

    """

    css_class = "govuk-tabs__panel"
    link_template = "%s/layout/tab-link.html"

    def __init__(self, name, *fields, **kwargs):
        super().__init__(*fields, **kwargs)
        self.name = name
        if "css_id" in kwargs:
            self.css_id = kwargs["css_id"]
        if not self.css_id:
            self.css_id = slugify(self.name)

    def render_link(self, template_pack=TEMPLATE_PACK):
        link_template = self.link_template % template_pack
        return render_to_string(link_template, {"link": self})
