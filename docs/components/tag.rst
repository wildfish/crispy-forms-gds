.. _Tag: https://design-system.service.gov.uk/components/tag/

###
Tag
###
A `Tag`_ is general used to report status. ::

    from django import forms
    from django.utils.safestring import mark_safe

    from crispy_forms_gds.helper import FormHelper
    from crispy_forms_gds.layout import HTML, Layout, Colour


    class TagForm(forms.Form):
        def __init__(self, *args, **kwargs):
            super(TagForm, self).__init__(*args, **kwargs)

            headings = ["Name of user", "status"]
            statuses = [
                ["Rachel Silver", mark_safe(HTML.tag("Pending", Colour.BLUE).html)],
                ["Jesse Smith", mark_safe(HTML.tag("Inactive", Colour.PURPLE).html)],
                ["Joshua Wessel ", mark_safe(HTML.tag("Active", Colour.GREEN).html)],
                ["Tim Harvey", mark_safe(HTML.tag("Blocked", Colour.RED).html)],
                ["Rachael Pepper", mark_safe(HTML.tag("Disabled", Colour.GREY).html)],
                ["Stuart Say", mark_safe(HTML.tag("Declined", Colour.ORANGE).html)],
                ["Laura Frith", mark_safe(HTML.tag("Waiting", Colour.PINK).html)],
                ["Emma Tennant", mark_safe(HTML.tag("New", Colour.TURQUOISE).html)],
                ["Nigel Starmer", mark_safe(HTML.tag("Delayed", Colour.YELLOW).html)],
            ]

            self.helper = FormHelper()
            self.helper.layout = Layout(HTML.table(headings, statuses))

You can see this form live in the Demo site.

Here we had to force render the tags then use ``mark_safe`` so the HTML could be
displayed within a table. That means, right now, you can't put layout objects
in tables. We are not too bothered since the Design System in intended to steer
you away from such shenanigans but we'll fix this in the future.

The contents of a ``TabPanel`` can be any set of Fields, HTML content,
LayoutObject or composed layout. You cannot nest sets of tabs. It works
visually, although the appearance is a little cluttered, however the
javascript that controls the switching between tabs does not work.

