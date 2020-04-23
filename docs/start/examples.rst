.. _Components: https://design-system.service.gov.uk/components
.. _Error summary: https://design-system.service.gov.uk/components/error-summary/

========
Examples
========
You use crispy-forms-gds just like a regular crispy form except you import
the various objects from ``crispy_forms_gds`` instead of crispy_forms. The
minimum viable form using this template pack is: ::

    from django import forms

    from crispy_forms_gds.helper import FormHelper
    from crispy_forms_gds.layout import Submit


    class MinimumForm(forms.Form):

        name = forms.CharField(
            label="Name",
            help_text="Your full name.",
            error_messages={
                "required": "Enter your name as it appears on your passport"
            }
        )

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper(self)
            self.helper.add_input(Submit("submit", _("Submit")))

All that is needed is to add the ``FormHelper`` class to the Form. Then in your
template add Design System `Error summary`_ and the ``crispy`` templatetag: ::

    {% load i18n crispy_forms_tags %}
    ...
    {% if form.helper.form_show_errors and form.errors %}
      {% include 'gds/layout/error_summary.html' %}
    {% endif %}
    ...
    {% crispy form %}
    ...

The template pack takes care of all the rendering so the displayed form follows
the Design System style and takes care of accessibility as well.

.. image:: form.png

There is support for all the Design System `Components`_ that you might expect
to encounter in a complex form with the exception of ``Date input`` which is on
the to-do list. There are some components like ``Summary list``, ``Table`` and
possibly, ``Skip link`` which might be useful but are not implemented currently
as they are probably rarely needed. The rest: ``Back link``, ``Breadcrumbs``,
``Header``, ``Footer`` and ``Phase banner`` are unlikely to ever appear in a form.

Many of the Design System Components can be configured, for example setting the
size of a label or the width of a text field. The simplest way is the crispy
way and use ``Layout`` objects to pass in the necessary parameters. Some of the
configuration involves setting CSS classes as well as template variables so
``crispy-forms-gds`` adds a set of class methods to the various layout objects
to make that easier. The following form is a big of a dog's breakfast in terms
of user experience but it does give you a good overview of just how little code
you need to create quite complex forms: ::

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
