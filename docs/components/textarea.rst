.. _Textarea: https://design-system.service.gov.uk/components/textarea/

########
Textarea
########
Adding a `Textarea`_ to a form is straightforward: ::

    from django import forms

    from crispy_forms_gds.helper import FormHelper
    from crispy_forms_gds.layout import Field, Layout, Size, Submit


    class TextareaForm(forms.Form):

        description = forms.CharField(
            label="Can you provide more detail?",
            widget=forms.Textarea,
            help_text="Do not include personal or financial information, like your "
            "National Insurance number or credit card details.",
            error_messages={"required": "Enter a short description of your application"},
        )

        def __init__(self, *args, **kwargs):
            super(TextareaForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(
                Field.textarea(
                    "description",
                    label_size=Size.LARGE,
                    label_tag="h2",
                    rows=3,
                    max_words=100,
                ),
                Submit("submit", "Submit"),
            )

You can see this form live in the Demo site.

The ``HTML`` class simplifies the process of setting the attributes and template
variables needed to render a ``<textarea>``. Here we assume the textarea is going
to be part of a multi-page form and displayed on a page by itself so we change the
size of the label and promote it to be the page header by wrapping it in an ``<h1>``
heading. Also we set the number of rows to 3. Django renders textareas with a
default of 10 rows but that is more than we need right now.

If that seems a little complicated, we could have just added the name of the
field to the ``Layout``: ::

        self.helper.layout = Layout(
            "description",
            Submit("submit", "Submit"),
        )

