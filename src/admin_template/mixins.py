from django.views.generic.base import ContextMixin
from typing import Any, Dict


class SideBarMixIn(ContextMixin):
    sidebar = None

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        if self.sidebar:
            context["sidebar_config"] = self.sidebar
        else:
            raise ValueError("sidebar in the view-class must be set.")
        return context
