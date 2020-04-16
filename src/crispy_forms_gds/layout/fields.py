from crispy_forms import layout as crispy_forms_layout


class Field(crispy_forms_layout.Field):
    template = "gds/field.html"


class Hidden(crispy_forms_layout.Hidden):
    pass
