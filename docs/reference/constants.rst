.. include:: ../conf.rst

=========
Constants
=========

The Design System sets the colour, font-size and width of fields using CSS classes.
Rather than deal with the CSS directly the template pack provides a set of (python)
classes with constants for each of the values. After all, who wants to be typing
something like ``govuk-!-width-three-quarters`` every time they want to set the width
of a field?. The constants are translated into the respective CSS class when a widget
is rendered.


Colours
=======

A set of constants defining the names for colours.

:colour-blue:`BLUE`

:colour-green:`GREEN`

:colour-grey:`GREY`

:colour-orange:`ORANGE`

:colour-pink:`PINK`

:colour-purple:`PURPLE`

:colour-red:`RED`

:colour-turquoise:`TURQUOISE`

:colour-yellow:`YELLOW`

Currently, ``Tag`` is the only component that explicitly sets a colour.
For everything else the colour is set in the stylesheet.

.. sourcecode:: django

    HTML.tag("Pending", Colour.BLUE)

The colour value is a simple string, e.g. ``'blue'`` The class method
converts it into the respective CSS class, e.g. ``govuk-tag--blue``.

If a new class is added but is has not been added to the template pack,
then just pass the name:

.. sourcecode:: django

    HTML.tag("Pending", 'lilac')


Font sizes
==========

A set of constants for setting the size of labels, legends or headings.

:font-small:`SMALL`

:font-medium:`MEDIUM`

:font-large:`LARGE`

:font-extra-large:`EXTRA LARGE`

Set the label size for a Text input:

.. sourcecode:: django

    Field.text("name", label_size=Size.SMALL)

Set the legend size for a set of checkboxes:

.. sourcecode:: django

    Field.checkboxes("multiple", legend_size=Size.MEDIUM)


Fixed widths
============

A set of constants for setting the width of a Text inputs to a fixed
number of characters.

TWO
  Set the Text input to be 2 characters wide.

THREE
  Set the Text input to be 3 characters wide.

FOUR
  Set the Text input to be 4 characters wide.

FIVE
  Set the Text input to be 5 characters wide.

TEN
  Set the Text input to be 10 characters wide.

TWENTY
  Set the Text input to be 20 characters wide.

THIRTY
  Set the Text input to be 30 characters wide.

.. sourcecode:: django

    Field.text("phone", field_width=Fixed.TWENTY)

The constant is just an integer. The ``Field`` class method converts
this into the respective Design System CSS class, for example
``govuk-input--width-20``.

You always have the option of adding the CSS class to the field:

.. sourcecode:: django

    Field.text("phone", css_class="govuk-input--width-20")

If the fixed width is not supported by the Design System then the text field
will take up the full width of the parent container.


Fluid widths
============

A set of constants for setting a fluid width on Text inputs.

ONE_QUARTER
  Set the Text input to be 25% of the width of the parent.

ONE_THIRD
  Set the Text input to be 33% of the width of the parent.

ONE_HALF
  Set the Text input to be 50% of the width of the parent.

TWO_THIRDS
  Set the Text input to be 66% of the width of the parent.

THREE_QUARTERS
  Set the Text input to be 75% of the width of the parent.

FULL
  Set the Text input to be 100% of the width of the parent.

.. sourcecode:: django

    Field.text("name", field_width=Fluid.TWO_THIRDS),

The constant is just a simple string, e.g. ``'two-thirds'``. The ``Field``
class method converts this into the respective Design System CSS class,
for example ``govuk-!-width-two-thirds``.

As with fixed widths, you always have the option of adding the CSS
class to the field:

.. sourcecode:: django

    Field.text("phone", css_class="govuk-!-width-two-thirds")

If the width is not supported by the Design System then the text field
will take up the full width of the parent container.
