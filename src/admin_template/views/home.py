from typing import Any, Dict
from admin_template.views.generic import SidebarTemplateView


class HomeView(SidebarTemplateView):
    template_name = "admin_template/home.html"
