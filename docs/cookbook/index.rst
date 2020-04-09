.. _GOV.UK Design System: https://design-system.service.gov.uk/
.. _Wildfish: https://wildfish.com/

Introduction
============
This cookbook takes you through the **Components** and **Patterns** sections
of the `GOV.UK Design System`_ guide and shows you how to write forms that
are fully compliant with Design System styles and accessibility guidelines.

Each sections has snippets of code that show how to render the various
components and patterns. The goal is to keep life simple so Django Forms and
Fields are used first, with the ``crispy-forms-gds`` template pack doing
the heavy-lifting when the form is rendered in a template.

The cookbook is constantly evolving. As lazy developers, whenever we find
there is too much code being written, generally that's a signal that some
functionality needs to be moved into custom Layout or Widget classes and
these will be added to the template pack as needed. The same goes for any
projects that use this template pack. If you find that creating a form,
which renders beautifully in the Design System, is taking too many keystrokes
to write, send in an example and we'll get it coded up to make your life as
simple as we can.

\- Brought to you by the Crispy Formers at `Wildfish`_.

