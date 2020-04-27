from django.template.loader import render_to_string
from django.utils.text import slugify

from crispy_forms import layout as crispy_forms_layout
from crispy_forms.utils import TEMPLATE_PACK, flatatt, render_field


class Div(crispy_forms_layout.Div):
    pass


class Accordion(Div):
    """
    Accordion menu object. It wraps `AccordionSection` objects in a container::

        Accordion(
            AccordionSection("group name", "form_field_1", "form_field_2"),
            AccordionSection("another group name", "form_field")
        )
    """

    template = "%s/accordion.html"

    def __init__(self, *fields, **kwargs):
        super().__init__(*fields, **kwargs)
        self.fields = list(fields)

        if hasattr(self, "css_class") and "css_class" in kwargs:
            self.css_class += " %s" % kwargs.pop("css_class")
        if not hasattr(self, "css_class"):
            self.css_class = kwargs.pop("css_class", None)

        self.css_id = kwargs.pop("css_id", "")
        self.template = kwargs.pop("template", self.template)
        self.flat_attrs = flatatt(kwargs)

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK, **kwargs):
        content = ""
        for group in self.fields:
            content += render_field(
                group, form, form_style, context, template_pack=template_pack, **kwargs
            )
        template = self.get_template_name(template_pack)
        context.update({"accordion": self, "content": content})
        return render_to_string(template, context.flatten())


class AccordionSection(Div):
    """
    Accordion Section (pane) object. It wraps given fields inside an accordion
    tab. It takes accordion tab name as first argument::

        AccordionSection("section_name", "form_field_1", "form_field_2")
    """

    template = "%s/accordion-group.html"
    data_parent = ""  # accordion parent div id.
    css_class = ""

    def __init__(self, name, *fields, **kwargs):
        super().__init__(*fields, **kwargs)
        self.name = name
        if not self.css_id:
            self.css_id = slugify(self.name)

    def __contains__(self, field_name):
        """
        check if field_name is contained within tab.
        """
        return field_name in map(lambda pointer: pointer[1], self.get_field_names())

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK, **kwargs):
        return super().render(form, form_style, context, template_pack)


class Fieldset(crispy_forms_layout.LayoutObject):
    """
    A layout object for displaying groups of fields with a main title.

    Example::

        Fieldset('form_field_1', 'form_field_2')
        Fieldset('form_field_1', 'form_field_2', legend="fieldset_title")
        Fieldset('form_field_1', 'form_field_2', legend="fieldset_title", legend_tag="h1")
        Fieldset('form_field_1', 'form_field_2', legend="fieldset_title", legend_size="xl")

   """

    css_class = "govuk-fieldset"
    template = "%s/layout/fieldset.html"

    def __init__(
        self, *fields, legend=None, legend_size=None, legend_tag=None, **kwargs
    ):
        self.fields = list(fields)
        self.context = {
            "legend": legend,
            "legend_size": legend_size,
            "legend_tag": legend_tag,
        }
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

    Example::

        Tabs(
            TabPane('tab_name_1', 'form_field_1', 'form_field_2'),
            TabPane('tab_name_2', 'form_field_3')
        )
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

    Example::

        TabPanel('tab_name', 'form_field_1', 'form_field_2', 'form_field_3')
    """

    css_class = "govuk-tabs__panel"
    link_template = "%s/layout/tab-link.html"

    def __init__(self, name, *fields, **kwargs):
        super().__init__(*fields, **kwargs)
        self.name = name
        if not self.css_id:
            self.css_id = slugify(self.name)

    def render_link(self, template_pack=TEMPLATE_PACK):
        link_template = self.link_template % template_pack
        return render_to_string(link_template, {"link": self})
