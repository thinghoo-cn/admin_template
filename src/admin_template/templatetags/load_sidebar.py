import datetime

from django import template

from admin_template.sidebar import HeaderList

register = template.Library()


@register.simple_tag(takes_context=True)
def load_sidebar(context, url):
    context.sidebar = HeaderList.to_django_context()
