from django import template


register = template.Library()


@register.inclusion_tag("gds/layout/error_summary.html")
def error_summary(form):
    return {"form": form}
