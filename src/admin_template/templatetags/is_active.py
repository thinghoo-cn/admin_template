import datetime
from django import template


register = template.Library()


@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)


@register.simple_tag(takes_context=True)
def is_active(context, url):
    if url == "/":
        if context.request.path == url:
            return "active"
        else:
            return ""

    if context.request.path.startswith(url):
        return "active"
    return ""
