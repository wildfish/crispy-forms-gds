from django.template.loader import render_to_string
from django.utils.text import slugify

import crispy_forms
from crispy_forms import layout as crispy_forms_layout
from crispy_forms.utils import TEMPLATE_PACK, flatatt, render_field

from crispy_forms_gds.layout import Size


class Div(crispy_forms_layout.Div):
    """
    A layout object for displaying a general-purpose Div. This is not
    a Design System component but is included as it's a basic part of
    ``django-crispy-forms``.

    Although there is the Fieldset component for grouping fields together
    a Div is quite useful when you just need to add some spacing between
    elements.

    Examples::

        Div("name", "email", "phone", css_class="govuk-!-margin-bottom-5")
        Div("street", "city", "post_code")

    Arguments:
        css_id (str, optional): an unique identifier for the <div>. Generally
            you will need to set this if you need to add some javascript or
            very specific styling.

        css_class (str, optional): the names of one or more CSS classes that
            will be added to the <div>. This parameter is for any styling you
            want to apply. Nothing is added by default.

        template (str, optional): the path to a template that overrides the
            one normally used.

        *fields: a list of layout objects - fields, buttons, HTML,
            etc. that displayed inside the <div> element.

        **kwargs: any additional attributes you want to add to the parent
            <div>.

    """

    pass


class Accordion(Div):
    """
    .. _Accordion: https://design-system.service.gov.uk/components/accordion/

    A layout object for displaying an `Accordion`_ component.

    Accordion is the parent object to which you add an ``AccordionSection`` for
    each of the panels you want to display.

    Examples::

        Accordion(
            AccordionSection("title_1", "form_field_1", "form_field_2"),
            AccordionSection("title_2", "form_field_3")
        )

        Accordion(
            AccordionSection("title", "form_field_1", "form_field_2"),
            css_id="accordion-1"
        )

    Arguments:
        css_id (str, optional): an unique identifier for the accordion. The
            default is "accordion". You will need to set this if you have more
            than one accordion on a page.

        css_class (str, optional): the names of one or more CSS classes that
            will be added to the parent <div>. The basic Design System CSS
            classes will be added automatically. This parameter is for any
            extra styling you want to apply.

        template (str, optional): the path to a template that overrides the
            one normally used the accordion.

        *fields: a list of AccordionSection objects that are the panels
            that make up this accordion.

        **kwargs: any additional attributes you want to add to the parent
            <div>.

    """

    template = "%s/accordion.html"

    def __init__(self, *fields, **kwargs):
        super().__init__(*fields, **kwargs)
        if not self.css_id:
            self.css_id = "accordion"


def accordion_render_v1(
    self, form, form_style, context, template_pack=TEMPLATE_PACK, **kwargs
):
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


def accordion_render_v2(self, form, context, template_pack=TEMPLATE_PACK, **kwargs):
    content = ""
    for index, group in enumerate(self.fields, start=1):
        context["index"] = index
        context["parent"] = self.css_id
        content += render_field(
            group, form, context, template_pack=template_pack, **kwargs
        )
    template = self.get_template_name(template_pack)
    context.update({"accordion": self, "content": content})
    return render_to_string(template, context.flatten())


if crispy_forms.__version__.startswith("1."):
    setattr(Accordion, "render", accordion_render_v1)
else:
    setattr(Accordion, "render", accordion_render_v2)


class AccordionSection(Div):
    """
    .. _Accordion: https://design-system.service.gov.uk/components/accordion/

    A layout object for displaying a action in an `Accordion`_ component.

    Examples::

        AccordionSection("title", "form_field_1", "form_field_2")

        AccordionSection(
            "title",
            "form_field_1",
            summary="A short description of the contents"
        )

    Arguments:
        name (str): the title of the section.

        summary (str, optional): a short description of the section's contents.

        css_id (str, optional): an unique identifier for the section. This is
            included as an AccordionSection is just a specialised Div. It is
            a basic LayoutObject param and should never have to set it.

        css_class (str, optional): the names of one or more CSS classes that
            will be added to the section <div>. The basic Design System CSS
            classes will be added automatically. This parameter is for any
            extra styling you want to apply.

        template (str, optional): the path to a template that overrides the
            one used to render a section.

        *fields: a list of layout objects objects that make up the section
            contents.

        **kwargs:  any additional attributes you want to add to the section
            <div>.

    """

    template = "%s/accordion-group.html"

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


def accordion_section_render_v1(
    self, form, form_style, context, template_pack=TEMPLATE_PACK, **kwargs
):
    self.index = context.get("index", None)
    self.parent = context.get("parent")
    fields = self.get_rendered_fields(
        form, form_style, context, template_pack, **kwargs
    )
    template = self.get_template_name(template_pack)
    return render_to_string(template, {"div": self, "fields": fields})


def accordion_section_render_v2(
    self, form, context, template_pack=TEMPLATE_PACK, **kwargs
):
    self.index = context.get("index", None)
    self.parent = context.get("parent")
    fields = self.get_rendered_fields(form, context, template_pack, **kwargs)
    template = self.get_template_name(template_pack)
    return render_to_string(template, {"div": self, "fields": fields})


if crispy_forms.__version__.startswith("1."):
    setattr(AccordionSection, "render", accordion_section_render_v1)
else:
    setattr(AccordionSection, "render", accordion_section_render_v2)


class Fieldset(crispy_forms_layout.LayoutObject):
    """
    A layout object for displaying groups of fields.

    The contents of a Fieldset are be one or more LayoutObjects: fields, buttons,
    composed layouts, etc. You can give the <fieldset> a <legend> title, set the size
    of the font used and wrap the <legend> in a heading tag if necessary.

    Examples::

        Fieldset('form_field_1', 'form_field_2')
        Fieldset('form_field_1', 'form_field_2', legend="title")
        Fieldset('form_field_1', 'form_field_2', legend="title", legend_tag="h1")
        Fieldset('form_field_1', 'form_field_2', legend="title", legend_size="xl")

    Arguments:
        legend (str, optional): the title displayed in a <legend>.

        legend_size (str, optional): the size of the title: 's', 'm', 'l' or
            'xl'. It's more readable if you use the contants on the ``Size`` class.

        legend_tag (str, optional): an HTML tag that wraps the <legend>. Typically
            this is 'h1' so the <legend> also acts as the page title.

        css_id (str, optional): an unique identifier for the fieldset.

        css_class (str, optional): the names of one or more CSS classes that
            will be added to the <fieldset>. The basic Design System CSS
            classes will be added automatically. This parameter is for any
            extra styling you want to apply.

        template (str, optional): the path to a template that overrides the
            one provided by the template pack.

        *fields: a list of LayoutObjects objects that make up the Fieldset contents.

        **kwargs:  any additional attributes you want to add to the <fieldset>.

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


def fieldset_render_v1(
    self, form, form_style, context, template_pack=TEMPLATE_PACK, **kwargs
):
    fields = self.get_rendered_fields(
        form, form_style, context, template_pack, **kwargs
    )
    context = {
        "fieldset": self,
        "fields": fields,
    }
    context.update(self.context)
    template = self.get_template_name(template_pack)
    return render_to_string(template, context)


def fieldset_render_v2(self, form, context, template_pack=TEMPLATE_PACK, **kwargs):
    fields = self.get_rendered_fields(form, context, template_pack, **kwargs)
    context = {
        "fieldset": self,
        "fields": fields,
    }
    context.update(self.context)
    template = self.get_template_name(template_pack)
    return render_to_string(template, context)


if crispy_forms.__version__.startswith("1."):
    setattr(Fieldset, "render", fieldset_render_v1)
else:
    setattr(Fieldset, "render", fieldset_render_v2)


class Tabs(Div):
    """
    A layout object for displaying a set of tabs.

    ``Tabs`` contains a list of ``TabPanels`` which in turn contains the
    list of fields and other layout objects which make up the content of
    each tab.

    Examples::

        Tabs(
            TabPane('tab_name_1', 'form_field_1', 'form_field_2'),
            TabPane('tab_name_2', 'form_field_3')
        )

    Arguments:
        css_id (str, optional): an unique identifier for the parent <div>.

        css_class (str, optional): the names of one or more CSS classes that
            will be added to the parent <div>. The basic Design System CSS
            classes will be added automatically. This parameter is for any
            extra styling you want to apply.

        template (str, optional): the path to a template that overrides the
            one provided by the template pack.

        *fields: a list of TabPanel objects that make up the set of tabs.

        **kwargs:  any additional attributes you want to add to the parent
            <div>.

    """

    template = "%s/layout/tabs.html"


def tabs_render_v1(
    self, form, form_style, context, template_pack=TEMPLATE_PACK, **kwargs
):
    content = self.get_rendered_fields(form, form_style, context, template_pack)
    links = "".join(tab.render_link(template_pack) for tab in self.fields)
    context.update({"tabs": self, "links": links, "content": content})
    template = self.get_template_name(template_pack)
    return render_to_string(template, context.flatten())


def tabs_render_v2(self, form, context, template_pack=TEMPLATE_PACK, **kwargs):
    content = self.get_rendered_fields(form, context, template_pack)
    links = "".join(tab.render_link(template_pack) for tab in self.fields)
    context.update({"tabs": self, "links": links, "content": content})
    template = self.get_template_name(template_pack)
    return render_to_string(template, context.flatten())


if crispy_forms.__version__.startswith("1."):
    setattr(Tabs, "render", tabs_render_v1)
else:
    setattr(Tabs, "render", tabs_render_v2)


class TabPanel(Div):
    """
    A layout object that displays the contents of each pane in a set of tabs.

    Examples::

        TabPanel('tab_name', 'form_field_1', 'form_field_2', 'form_field_3')

    Arguments:
        name (str): the title of the panel.

        css_id (str, optional): an unique identifier for the parent <div>.
            If you don't set this then the slugified title is used for the
            id attribute. You must set this if you have more than one set
            of tabs on a page with the same set of titles.

        css_class (str, optional): the names of one or more CSS classes that
            will be added to the parent <div>. The basic Design System CSS
            classes will be added automatically. This parameter is for any
            extra styling you want to apply.

        template (str, optional): the path to a template that overrides the
            one provided by the template pack.


        *fields: a list of layout objects that make up the contents of the panel.

        **kwargs:  any additional attributes you want to add to the <div>
            element used for create the tab panel.

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


class ConditionalQuestion(crispy_forms_layout.TemplateNameMixin):
    """
    A layout object that wraps field(s) around a conditional question

    Examples::

        ConditionalQuestion(
            'Contact me by phone',
            'mobile_number',
            'home_number',
        )

    Arguments:
        value (str): the label value of the radio choice.

        *fields: a list of layout objects that are revealed on selection of the
            choice.
    """

    template = "%s/layout/conditional_question.html"

    def __init__(self, value, *fields):
        self.value = value
        self.fields = list(fields)


def conditional_question_render_v1(
    self, bound_field, form, form_style, context, template_pack=TEMPLATE_PACK, **kwargs
):
    template = self.get_template_name(template_pack)

    mapped_choices = {choice[1]: choice for choice in bound_field.field.choices}
    value = self.value
    choice = mapped_choices[value]
    position = list(mapped_choices.keys()).index(self.value)

    conditional_content = ""
    for field in self.fields:
        conditional_content += render_field(
            field, form, form_style, context, template_pack=template_pack, **kwargs
        )

    context.update(
        {
            "choice": choice,
            "field": bound_field,
            "position": position,
            "conditional_content": conditional_content,
        }
    )

    return render_to_string(template, context.flatten())


def conditional_question_render_v2(
    self, bound_field, form, context, template_pack=TEMPLATE_PACK, **kwargs
):
    template = self.get_template_name(template_pack)

    mapped_choices = {choice[1]: choice for choice in bound_field.field.choices}
    value = self.value
    choice = mapped_choices[value]
    position = list(mapped_choices.keys()).index(self.value)

    conditional_content = ""
    for field in self.fields:
        conditional_content += render_field(
            field, form, context, template_pack=template_pack, **kwargs
        )

    context.update(
        {
            "choice": choice,
            "field": bound_field,
            "position": position,
            "conditional_content": conditional_content,
        }
    )

    return render_to_string(template, context.flatten())


if crispy_forms.__version__.startswith("1."):
    setattr(ConditionalQuestion, "render", conditional_question_render_v1)
else:
    setattr(ConditionalQuestion, "render", conditional_question_render_v2)


class ConditionalRadios(crispy_forms_layout.TemplateNameMixin):
    """
    A layout object that wraps radio buttons with one or more being a
    conditional question which reveals fields once selected

    Examples::

        ConditionalRadios(
            'how_to_contact_me',
            ConditionalQuestion(
                'Email',
                'email_address',
            ),
            ConditionalQuestion(
                'Telephone',
                'telephone_number',
            )
            'Do not contact me',
        )

    Arguments:
        field (str): the radio field for conditional revelations

        *fields: a list of either ConditionalQuestion objects or the label
            of a field without any conditional fields
    """

    template = "%s/layout/conditional_radios.html"

    def __init__(self, field, *choices):
        if not isinstance(field, str):
            raise TypeError(
                f"{self.__class__.__name__} only accepts field as a string parameter"
            )

        self.field = field
        self.choices = list(choices)


def conditional_radios_render_choices_v1(
    self,
    bound_field,
    form,
    form_style,
    context,
    template_pack=TEMPLATE_PACK,
    **kwargs,
):
    to_render = []
    for value in self.choices:
        if not isinstance(value, (str, ConditionalQuestion)):
            raise TypeError("Only accepts values of type str or ConditionalQuestions")
        if isinstance(value, str):
            value = ConditionalQuestion(value)
        to_render.append(value)

    return "".join(
        [
            t.render(bound_field, form, form_style, context, template_pack, **kwargs)
            for t in to_render
        ]
    )


def conditional_radios_render_choices_v2(
    self,
    bound_field,
    form,
    context,
    template_pack=TEMPLATE_PACK,
    **kwargs,
):
    to_render = []
    for value in self.choices:
        if not isinstance(value, (str, ConditionalQuestion)):
            raise TypeError("Only accepts values of type str or ConditionalQuestions")
        if isinstance(value, str):
            value = ConditionalQuestion(value)
        to_render.append(value)

    return "".join(
        [
            t.render(bound_field, form, context, template_pack, **kwargs)
            for t in to_render
        ]
    )


def conditional_radios_render_v1(
    self, form, form_style, context, template_pack=TEMPLATE_PACK, **kwargs
):
    template = self.get_template_name(template_pack)

    bound_field = form[self.field]

    context.update(
        {
            "choices": self.render_choices(
                bound_field, form, form_style, context, template_pack, **kwargs
            )
        }
    )

    return render_to_string(template, context.flatten())


def conditional_radios_render_v2(
    self, form, context, template_pack=TEMPLATE_PACK, **kwargs
):
    template = self.get_template_name(template_pack)

    bound_field = form[self.field]

    context.update(
        {
            "choices": self.render_choices(
                bound_field, form, context, template_pack, **kwargs
            )
        }
    )

    return render_to_string(template, context.flatten())


if crispy_forms.__version__.startswith("1."):
    setattr(ConditionalRadios, "render_choices", conditional_radios_render_choices_v1)
    setattr(ConditionalRadios, "render", conditional_radios_render_v1)
else:
    setattr(ConditionalRadios, "render_choices", conditional_radios_render_choices_v2)
    setattr(ConditionalRadios, "render", conditional_radios_render_v2)
