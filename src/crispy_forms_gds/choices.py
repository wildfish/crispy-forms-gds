import django

"""
Choice is used for the items in the choices attribute of a form field.

It emulates the tuple that returns the field value and the label and
supports the attributes needed to display hints and dividers.

Examples: ::

    METHODS = (
        Choice("email", "Email"),
        Choice("phone", "Phone", hint="Select this only if you have a mobile phone"),  # noqa
        Choice("text", "Text message"),
    )

    method = forms.MultipleChoiceField(
        choices=METHODS,
        widget=forms.CheckboxSelectMultiple,
        label="How would you like to be contacted?",
        help_text="Select all options that are relevant to you.",
        error_messages={"required": "Enter the ways to contact you"},
    )

Args:
    value (int, str): the value for the checkbox or radio button.

    label (str): the label for the checkbox or radio button.

    **kwargs: additional attributes to display for the checkbox or radio button.
        Two attributes are supported: a `hint` that is displayed below the label
        and a 'divider' that is displayed after the radio button.

"""

# Django 5+ internals changed the way the choices on a ChoiceField are
# normalised. Changing the parent class to a Promise preserves the hint
# and divider attributes so the field can be rendered.

if django.VERSION[0] < 5:

    class Choice:

        def __init__(self, value, label, **kwargs):
            self.value = value
            self.label = label
            for key, value in kwargs.items():
                setattr(self, key, value)

        def __iter__(self):
            return iter((self.value, self.label))

        def __getitem__(self, index):
            return (self.value, self.label)[index]

else:

    class Choice(django.utils.functional.Promise):

        def __init__(self, value, label, **kwargs):
            self.value = value
            self.label = label
            for key, value in kwargs.items():
                setattr(self, key, value)

        def __iter__(self):
            return iter((self.value, self.label))

        def __getitem__(self, index):
            return (self.value, self.label)[index]
