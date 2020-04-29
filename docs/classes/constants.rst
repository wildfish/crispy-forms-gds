=======================
Colours, Sizes & Widths
=======================

The Design System sets the colour, font-size and width of fields using CSS classes.
Rather than deal with the CSS directly the template pack provides a set of (python)
classes with constants for each of the values. After all, who wants to be typing
something like ``govuk-!-width-three-quarters`` every time they want to set the width
of a field?. The constants are translated into the respective CSS class when a widget
is rendered.


Colour
======

.. autoclass:: crispy_forms_gds.layout.Colour
   :members:


Font Sizes
==========

.. autoclass:: crispy_forms_gds.layout.Size
   :members:
   :member-order: bysource


Fixed Widths
============

.. autoclass:: crispy_forms_gds.layout.Fixed
   :members:
   :member-order: bysource


Fluid Widths
============

.. autoclass:: crispy_forms_gds.layout.Fluid
   :members:
   :member-order: bysource

