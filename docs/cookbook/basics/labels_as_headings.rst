##################################
Making labels and legends headings
##################################
When there is only one question on a page you can make the label associated with
a field the title of the page. To do that the field label or legend needs to be
wrapped in an ``<h1>`` element - it's not enough just to change the size of the
label or omit the label and add the ``<h1>`` tag instead, as that will confuse
screen readers.

You can do this easily enough on the ``Field`` class methods but setting the
``label_is_heading`` argument to ``True``: ::

    from django import forms

    from crispy_forms_gds.helper import FormHelper
    from crispy_forms_gds.layout import Field, Layout, Submit


    class CookbookForm(forms.Form):
        name = forms.CharField(label="Name")

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(
                Field.text("name", label_size="l", label_is_heading=True),
                Submit("submit", "Submit"),
            )

You also should set the label size since the default font does not look impressive
at all.

The code works using a conditional statement in the template to wrap the ``<label>``
or ``<legend>`` in the ``<h1>`` tag so you need to use the context if you want to
set this manually on a ``Field`` instance: ::

    from django import forms

    from crispy_forms_gds.helper import FormHelper
    from crispy_forms_gds.layout import Field, Layout, Size, Submit


    class CookbookForm(forms.Form):
        name = forms.CharField(label="Name")

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(
                Field("name", context={
                    "field_label_size": Size.LARGE,
                    "field_label_is_heading": True
                }),
                Submit("submit", "Submit")
            )
