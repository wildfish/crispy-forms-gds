from datetime import date

from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

from crispy_forms_gds.widgets import DateInputWidget


class DateInputField(forms.MultiValueField):
    """
    .. _Date input: https://design-system.service.gov.uk/components/date-input/

    DateInputField is a MultiValueField for dates with separate fields for
    the day, month and year. It is used to implement the `Date input`_
    component.

    The attribute ``require_all_fields`` determines where blank fields are
    handled. If ``True`` and if all of the day, month or year fields are
    blank a ``required`` error is raised. If any of the fields are blank
    then an ``incomplete`` error is raised, These errors are reported
    at the MultiValueField level - collectively - and so are not tied to
    any specific field. Generally, for the Design System, you will want to
    tie every error to a specific field. You can do that by setting
    ``require_all_fields`` to ``False`` when you create a Form. Then an
    error will be reported for each blank field. Which strategy to choose
    will probably depend in the application, some cases a general "one of
    the fields is blank" is sufficient and for other applications a detailed
    list of exactly what error occurred in what field will be more instructive.

    The error messages on the MultiValueField and in the validators on each
    sub-field are utterly generic and do not provide the clear guidance that
    is generally needed for public-facing applications. You should almost
    always override these with message tailored to your application so the
    user can receive clear and specific instruction on what the problem is
    and how it can be corrected.

    """

    widget = DateInputWidget

    def __init__(self, **kwargs):
        # Define one message for all fields.
        error_messages = {
            "required": "Enter the day, month and year",
            "incomplete": "Enter the day, month and year",
        }
        # Or define a different message for each field.
        fields = (
            forms.CharField(
                label=_("Day"),
                error_messages={"incomplete": "Enter the day of the month"},
                validators=[RegexValidator(r"^[0-9]+$", "Enter a valid date")],
            ),
            forms.CharField(
                label=_("Month"),
                error_messages={"incomplete": "Enter the month"},
                validators=[RegexValidator(r"^[0-9]+$", "Enter a valid month")],
            ),
            forms.CharField(
                label=_("Year"),
                error_messages={"incomplete": "Enter the year"},
                validators=[RegexValidator(r"^[0-9]+$", "Enter a valid year")],
            ),
        )

        super().__init__(error_messages=error_messages, fields=fields, **kwargs)

    def clean(self, value):
        """
        Validate the values entered into the day, month and year fields.

        Validate every value in the given list. A value is validated against
        the corresponding Field in self.fields.

        Normally, all errors are reported at the level of the MultiValueField.
        However the Design System requires that the Error Summary has links to
        tie an error to a specific field. To make that work the ValidationErrors
        for each field (day, month and year) are added to a list on the respective
        widgets as well as the error list on the (bound) field. This was the easiest
        way to get access to the errors for a specific field when the DateInputWidget
        on the MultiValueField is rendered.

        Args:
            value (list, tuple): the values entered into each field. The values are
                in the order the fields are added to the ``fields`` attribute.

        Raises:
            ValidationError: if any of the values fails the validation checks performed
                at the widget level or in this method.

        Returns:
             the value converted to a ``date``.

        """
        clean_data = []
        errors = []
        if self.disabled and not isinstance(value, list):
            value = self.widget.decompress(value)
        if not value or isinstance(value, (list, tuple)):
            if not value or not [v for v in value if v not in self.empty_values]:
                if self.required:
                    raise ValidationError(
                        self.error_messages["required"], code="required"
                    )
                else:
                    return self.compress((None, None, None))
        else:
            raise ValidationError(self.error_messages["invalid"], code="invalid")
        for i, field in enumerate(self.fields):
            field.widget.errors = []
            try:
                field_value = value[i]
            except IndexError:
                field_value = None
            if field_value in self.empty_values:
                if self.require_all_fields:
                    # Raise a 'required' error if the MultiValueField is
                    # required and any field is empty.
                    if self.required:
                        raise ValidationError(
                            self.error_messages["required"], code="required"
                        )
                elif field.required:
                    # Otherwise, add an 'incomplete' error to the list of
                    # collected errors and skip field cleaning, if a required
                    # field is empty.
                    if field.error_messages["incomplete"] not in errors:
                        errors.append(field.error_messages["incomplete"])
                        field.widget.errors.append(field.error_messages["incomplete"])
                    continue
            try:
                clean_data.append(field.clean(field_value))
            except ValidationError as e:
                # Collect all validation errors in a single list, which we'll
                # raise at the end of clean(), rather than raising a single
                # exception for the first error we encounter. Skip duplicates.
                errors.extend(m for m in e.error_list if m not in errors)
                field.widget.errors.extend(
                    m for m in e.messages if m not in field.widget.errors
                )
        if errors:
            raise ValidationError(errors)

        out = self.compress(clean_data)
        self.validate(out)
        self.run_validators(out)
        return out

    def compress(self, data_list):
        """
        Convert the values entered into the fields as a ``date``.

        Args:
            data_list (tuple): a 3-tuple the of values entered into the fields.

        Returns:
            the ``date`` for the values entered in the day, month and year fields.
                If any of the field are blank then None is returned.

        """
        day, month, year = data_list
        if day and month and year:
            try:
                return date(day=int(day), month=int(month), year=int(year))
            except ValueError as e:
                raise ValidationError(str(e)) from e
        else:
            return None
