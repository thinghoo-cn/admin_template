from django.views.generic import TemplateView
from admin_template.mixins import SideBarMixIn
from admin_template.sidebar import default_sidebar


class SidebarTemplateView(SideBarMixIn, TemplateView):
    sidebar = default_sidebar
