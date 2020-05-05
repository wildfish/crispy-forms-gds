from datetime import date

from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

from crispy_forms_gds.widgets import DateInputWidget


class DateInputField(forms.MultiValueField):
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
        Validate every value in the given list. A value is validated against
        the corresponding Field in self.fields.

        For example, if this MultiValueField was instantiated with
        fields=(DateField(), TimeField()), clean() would call
        DateField.clean(value[0]) and TimeField.clean(value[1]).

        Normally all errors are reported at the MultiValueField level. However
        the Error Summary component in the Design System requires an error to
        be tied to a specific field within the MultiValueField. So the clean
        method is overridden so when a ValidationError is raised by one of the
        constituent fields it is recorded on the respective widgets. When the
        Error Summary is rendered a custom templatetag generates the list of
        errors with the id of the widget that generated them. That allows a
        link to be generated that takes the user to the field that generated it.

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
                    return self.compress([])
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
        day, month, year = data_list
        if day and month and year:
            return date(day=int(day), month=int(month), year=int(year))
        else:
            return None
