.. _Date input: https://design-system.service.gov.uk/components/date-input/

##########
Date input
##########
The `Date input`_ component allow you to enter date with separate fields for
day, month and year: ::

    from django import forms
    from django.utils.translation import ugettext_lazy as _

    from crispy_forms_gds.fields import DateInputField
    from crispy_forms_gds.helper import FormHelper
    from crispy_forms_gds.layout import Layout, Submit


    class DateInputForm(forms.Form):

        date = DateInputField(
            label="When was your passport issued?",
            help_text="For example, 12 11 2007",
            require_all_fields=False,
        )

        def __init__(self, *args, **kwargs):
            super(DateInputForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout("date", Submit("submit", _("Submit")))

            self.fields["date"].fields[2].error_messages[
                "incomplete"
            ] = "The date your passport was issued must include a year"

You can see this form live in the Demo site.

There are two things to note in the above example. The first is that the field
attribute, ``require_all_fields`` is set to False. This is done to avoid getting
field-level errors mixed with errors from the separate day, month and year fields. For
example if ``require_all_fields`` is True and the user leaves the year field blank
then there will be a ``required`` error, "Enter the day, month and year" from the
date field and an "Enter the year" error from the year field. Setting ``require_all_fields``
to False means that any blank fields are validated at the child field level so
the types of errors from the parent field and those from the child fields are
more clearly distinguished. The second thing to note is that for almost all
applications you will have to override the error messages with something more
specific to the purpose of the form. The basic error messages on the field are
generic in nature: "Enter the month" which is clear but not very helpful.

IMPORTANT: The day, month and year fields use validators to check the values
entered by the user. You may need to update the validation error message or
even replace the validators entirely according to the needs of your application.
The exact configuration of this component might get revised once we have more
production experience in using it.
