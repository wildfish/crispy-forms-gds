#######################################
Changing the size of labels and legends
#######################################
A label for a field is displayed using the same font size as regular text.
The Design System supports four sizes which are relative to the default
size: 's' (small), 'm' (medium), 'l' (large) and 'xl' (extra-large).

As a convenience these values are defined in the ``Size`` class, but you
might find that using the string directly is just as readable.

There are two ways you can set the size of a label or legend:

1. Globally, for every field on a form.
2. Locally, for any field on a case-by-case basis.

To set the labels size globally, set the `label_size` attribute on the
``FormHelper`` class when you define the layout for a form: ::

    from django import forms

    from crispy_forms_gds.helper import FormHelper
    from crispy_forms_gds.layout import Size, Submit


    class CookbookForm(forms.Form):
        name = forms.CharField(label="Name")

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.label_size = Size.LARGE
            self.helper.add_input(Submit("submit", "Submit"))

To set the label size for an individual field, you can set the ``label_size``
argument on theField class methods: ::

    from django import forms

    from crispy_forms_gds.helper import FormHelper
    from crispy_forms_gds.layout import Field, Layout, Size, Submit


    class CookbookForm(forms.Form):
        name = forms.CharField(label="Name")

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(
                Field.text("name", label_size=Size.LARGE),
                Submit("submit", "Submit")
            )

Alternatively set the ``label_size`` template variable in the context when
creating a ``Field`` object directly: ::

    from django import forms

    from crispy_forms_gds.helper import FormHelper
    from crispy_forms_gds.layout import Field, Layout, Size, Submit


    class CookbookForm(forms.Form):
        name = forms.CharField(label="Name")

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(
                Field("name", context={"label_size": Size.LARGE}),
                Submit("submit", "Submit")
            )
