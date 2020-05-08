class Colour:
    """
    .. include:: ../conf.rst

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

    Examples:
        You pass the colour in the class method for generating a tag: ::

            HTML.tag("Pending", Colour.BLUE)

        If a new class is added but is has not been added to the template
        pack, then just pass the name: ::

            HTML.tag("Pending", 'lilac')

    """

    # Don't define the attribute here as you'll be forced to add the
    # type which makes the documentation a lot less readable

    BLUE = "blue"
    GREEN = "green"
    GREY = "grey"
    ORANGE = "orange"
    PINK = "pink"
    PURPLE = "purple"
    RED = "red"
    TURQUOISE = "turquoise"
    YELLOW = "yellow"

    _values = (BLUE, GREEN, GREY, ORANGE, PINK, PURPLE, RED, TURQUOISE, YELLOW)

    @classmethod
    def is_valid(cls, value):
        """Check whether a value is one of the pre-defined colours.

        Args:
            value (str): the name of the colour.

        Returns:
            True if the value equals one of the constants, False otherwise.

        """
        return value in cls._values

    @classmethod
    def for_tag(cls, value, validate=True):
        """
        Convert the colour name into a CSS class that can be added to a Tag
        component.

        Args:
            value: the colour.
            validate: check whether the colour is one of the pre-defined
                values. Defaults to True.

        Raises:
            ValueError: if validate is True and the colour is invalid.

        Returns:
            str: the CSS class used to set the tag colour.

        """
        if validate and not cls.is_valid(value):
            raise ValueError("Unexpected colour", value)
        return "govuk-tag--%s" % value


class Size:
    """
    .. include:: ../conf.rst

    A set of constants for setting the size of labels, legends or headings.

    Attributes:
        SMALL: :font-small:`SMALL`.
        MEDIUM: :font-medium:`MEDIUM`.
        LARGE: :font-large:`LARGE`.
        EXTRA_LARGE: :font-extra-large:`EXTRA LARGE`.

    Examples:
        Set the label size and heading level for a Text input (remember
        the heading level is the semantic level and not the size): ::

            Field.text("name", label_size=Size.SMALL, label_tag="h2")

        Set the legend size for a set of checkboxes: ::

            Field.checkboxes("multiple", legend_size=Size.MEDIUM)


    """

    # Don't define the attribute here as you'll be forced to add the
    # type which makes the documentation a lot less readable

    SMALL = "s"
    MEDIUM = "m"
    LARGE = "l"
    EXTRA_LARGE = "xl"

    _values = (SMALL, MEDIUM, LARGE, EXTRA_LARGE)

    @classmethod
    def is_valid(cls, value):
        """Check whether a value is one of the pre-defined sizes.

        Args:
            value (str): the size.

        Returns:
            True if the value equals one of the constants, False otherwise.

        """
        return value in cls._values

    @classmethod
    def for_label(cls, value, validate=True):
        """
        Convert the constant into a CSS class that can be used with a <label>.

        Args:
            value: the size.
            validate: check whether the size is one of the predefined
                values. Defaults to True.

        Raises:
            ValueError: if validate is True and the size in invalid.

        Returns:
            str: the CSS class used to set the font size for a label heading.

        """
        if validate and not cls.is_valid(value):
            raise ValueError("Unexpected size", value)
        return "govuk-label--%s" % value

    @classmethod
    def for_legend(cls, value, validate=True):
        """
        Convert the constant into a CSS class that can be used with a <legend>.

        Args:
            value: the size.
            validate: check whether the size is one of the pre-defined
                values. Defaults to True.

        Raises:
            ValueError: if validate is True and the size is invalid.

        Returns:
            str: the CSS class used to set the font size for a legend.

        """
        if validate and not cls.is_valid(value):
            raise ValueError("Unexpected size", value)
        return "govuk-fieldset__legend--%s" % value


class Fixed:
    """
    A set of constants for setting the width of a Text inputs to a fixed
    number of characters.

    Attributes:
        TWO: Set the Text input to be 2 characters wide.
        THREE: Set the Text input to be 3 characters wide.
        FOUR: Set the Text input to be 4 characters wide.
        FIVE: Set the Text input to be 5 characters wide.
        TEN: Set the Text input to be 10 characters wide.
        TWENTY: Set the Text input to be 20 characters wide.
        THIRTY: Set the Text input to be 30 characters wide.

    Examples:
        ::

            Field.text("phone", field_width=Fixed.TWENTY)
            Field.text("age", css_class=Fixed.for_input)

    """

    # Don't define the attribute here as you'll be forced to add the
    # type which makes the documentation a lot less readable

    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    TEN = 10
    TWENTY = 20
    THIRTY = 30

    _values = (TWO, THREE, FOUR, FIVE, TEN, TWENTY, THIRTY)

    @classmethod
    def is_valid(cls, value):
        """Check whether a value is one of the pre-defined values.

        Args:
            value: the width.

        Returns:
            True if the value equals one of the fixed widths, False otherwise.

        """
        return value in cls._values

    @classmethod
    def for_input(cls, value, validate=True):
        """
        Convert the fixed width into a CSS class.

        Args:
            value: the width.
            validate: check whether the width is a fixed value.

        Raises:
            ValueError: if validate is True and the value is invalid.

        Returns:
            str: the CSS class used to set the width of a Text input.

        """
        if validate and not cls.is_valid(value):
            raise ValueError("Unexpected fixed width", value)
        return "govuk-input--width-%d" % value


class Fluid:
    """
    A set of constants for setting a fluid width on Text inputs.

    Attributes:
        ONE_QUARTER: Set the Text input to be 25% of the width of the parent.
        ONE_THIRD: Set the Text input to be 33% of the width of the parent.
        ONE_HALF: Set the Text input to be 50% of the width of the parent.
        TWO_THIRDS: Set the Text input to be 66% of the width of the parent.
        THREE_QUARTERS: Set the Text input to be 75% of the width of the parent.
        FULL: Set the Text input to be 100% of the width of the parent.

    Examples:
        ::

            Field.text("name", field_width=Fluid.TWO_THIRDS),
            Field.text("email", css_class=Fluid.for_input('one-fifth', validate=False)),

    """

    # Don't define the attribute here as you'll be forced to add the
    # type which makes the documentation a lot less readable

    ONE_QUARTER = "one-quarter"
    ONE_THIRD = "one-third"
    ONE_HALF = "one-half"
    TWO_THIRDS = "two-thirds"
    THREE_QUARTERS = "three-quarters"
    FULL = "full"

    _values = (
        ONE_QUARTER,
        ONE_THIRD,
        ONE_HALF,
        TWO_THIRDS,
        THREE_QUARTERS,
        FULL,
    )

    @classmethod
    def is_valid(cls, value):
        """Check whether a value is one of the pre-defined values.

        Args:
            value: the width.

        Returns:
            True if the value equals one of the fixed widths, False otherwise.

        """
        return value in cls._values

    @classmethod
    def for_input(cls, value, validate=True):
        """
        Convert the fluid width into a CSS class.

        Args:
            value: the width.
            validate: check whether the width is a fluid value.

        Raises:
            ValueError: if validate is True and the width is not fluid.

        Returns:
            str: the CSS class used to set the width of a Text input.

        """
        if validate and not cls.is_valid(value):
            raise ValueError("Unexpected fluid width", value)
        return "govuk-!-width-%s" % value
