import warnings
from django.urls import include, path

from .views import about, home
from django.conf import settings

if settings.DEBUG:
    warnings.warn("If your are not developer of the admin_template, there is no need to include this urls.")


urlpatterns = [
    path("", home.HomeView.as_view(), name="home"),
    path("about/", about.about_page),
]
