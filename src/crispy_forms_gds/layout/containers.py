from crispy_forms import layout as crispy_forms_layout
from crispy_forms.utils import TEMPLATE_PACK, flatatt
from django.template.loader import render_to_string
from django.utils.text import slugify

from crispy_forms_gds.layout import Div


class Fieldset(crispy_forms_layout.LayoutObject):
    """
    A layout object for displaying groups of fields with a main title.

    Example::

        Fieldset('form_field_1', 'form_field_2')
        Fieldset('form_field_1', 'form_field_2', title="fieldset_title")
        Fieldset('form_field_1', 'form_field_2', title="fieldset_title", tag="h1")
        Fieldset('form_field_1', 'form_field_2', title="fieldset_title", size="xl")

   """

    css_class = "govuk-fieldset"
    template = "%s/layout/fieldset.html"

    def __init__(self, *fields, title=None, size=None, tag=None, **kwargs):
        self.fields = list(fields)
        self.context = {
            "legend_title": title,
            "legend_size": size,
            "legend_tag": tag,
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
