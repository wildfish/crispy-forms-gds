=======
Layouts
=======
The real power of the crispy way is the ability to define exactly how a form is
laid out in code rather than in HTML. The GOV.UK Design System adds a lot of attributes
and CSS classes to the basic HTML tags that make up a form. When you add all the
attributes needed for accessibility to ensure your forms are usable by as wide a
range of people as possible then the resultant HTML is hard to manage: ::

    <div id="div_id_name" class="govuk-form-group">
      <label for="id_name" class="govuk-label">
        Name
      </label>
      <div id="id_name_hint" class="govuk-hint">
        Help text
      </div>
      <input type="text" name="name"
             aria-describedby="id_name_hint"
             class="govuk-input"
             id="id_name">
    </div>

Now add in the markup needed to display an error: ::

    <div id="div_id_name" class="govuk-form-group govuk-form-group--error">
      <label for="id_name" class="govuk-label">
        Name
      </label>
      <div id="id_name_hint" class="govuk-hint">
        Help text
      </div>
      <span id="id_name_1_error" class="govuk-error-message">
        <span class="govuk-visually-hidden">Error:</span> Required error message
      </span>
      <input type="text" name="name"
             aria-describedby="id_name_hint id_name_1_error"
             class="govuk-input govuk-input--error"
             id="id_name">
    </div>

That's the absolute bare minimum needed to render a single text field and there's
no support for the error summary, autocomplete or other attributes to make the form
accessible. It's a lot of work and it's very easy to leave off a single attribute
that would render the form useless for people with screen readers, for example.

Layouts solve all these problems. The template pack supports all the components
available in the Design System so you can quickly and easily lay out a form and
any incidental content with a minimum of effort: ::

    from django import forms

    from crispy_forms_gds.helper import FormHelper
    from crispy_forms_gds.layout import (
        Button,
        Field,
        HTML,
        Layout,
        Tabs,
        TabPanel,
        Fluid,
        Size,
    )


    class CookbookForm(forms.Form):
        name = forms.CharField(
            label="Name",
            help_text="Your full name.",
            error_messages={"required": "Enter your name as it appears on your passport"},
        )

        email = forms.CharField(
            label="Email",
            help_text="Your email address.",
            error_messages={"required": "Enter your preferred email address"},
        )

        phone = forms.CharField(
            label="Phone",
            help_text="Your phone number, mobile or landline.",
            error_messages={"required": "Enter the number where we can contact you"},
        )

        method = forms.ChoiceField(
            label="Contact method",
            help_text="How can we contact you",
            error_messages={"required": "Enter the best way to contact you"},
            choices=(("email", "Email"), ("phone", "Phone"), ("text", "Text message")),
            widget=forms.CheckboxSelectMultiple,
        )

        skills = forms.CharField(
            label="Skills",
            help_text="Write a short summary of your main skills.",
            widget=forms.Textarea,
            error_messages={
                "required": "Enter the skills you can bring to this organisation"
            },
        )

        resume = forms.FileField(
            label="Resume",
            help_text="Upload your resume",
            error_messages={"required": "Upload an up to date copy of your resume"},
        )

        degree = forms.ChoiceField(
            label="Education",
            help_text="Do you hold a degree from a university or college?",
            choices=(("yes", "Yes"), ("no", "No"),),
            widget=forms.RadioSelect,
            error_messages={
                "required": "Enter whether you have a further education degree"
            },
        )

        level = forms.ChoiceField(
            label="Select",
            help_text="If you have a degree at what level is it?",
            choices=(
                ("", "Choose"),
                ("under", "Undergraduate degree"),
                ("masters", "Masters degree"),
                ("doctorate", "Ph.D."),
            ),
            widget=forms.Select,
        )

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.label_size = Size.MEDIUM
            self.helper.legend_size = Size.MEDIUM
            self.helper.layout = Layout(
                HTML("<h1>Application</h1>"),
                "name",
                Tabs(
                    TabPanel(
                        "Contact Details",
                        "email",
                        Field.text("phone", field_width=Fluid.ONE_HALF),
                        "method",
                    ),
                    TabPanel(
                        "Qualifications",
                        Field.text("skills", rows="5"),
                        "degree",
                        "level",
                        "resume",
                    ),
                ),
                Button.primary("apply", "Apply"),
            )

That's a slightly contrived example but it shows you how the various Design
System components can be used and configured in code.

Take a look at the source code for the Demo Site. There's the base template
for laying out the page but the main ``{% block %}`` for the page contents
is just: ::

    {% extends "components/base.html" %}
    {% load i18n crispy_forms_tags crispy_forms_gds_tags %}

    {% block content %}

      {% error_summary form %}

      <span class="govuk-caption-xl">
        {% trans 'Components' %}
      </span>
      <h1 class="govuk-heading-xl">
        {{ title }}
      </h1>

      <div class="govuk-body">
        {% crispy form %}
      </div>

    {% endblock %}

That's all the markup needed to display any of the forms in the Demo Site.
All the work is done in the form layouts. All the markup for accessibility
is already included in the template pack. You get 100% compliant forms, 100%
of the time. When that is replicated across all the projects that use the
GOV.UK Design System the savings in time and effort should be substantial.
