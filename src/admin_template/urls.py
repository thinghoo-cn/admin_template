from django.urls import include, path

from .views import about, home

urlpatterns = [
    path("", home.home_page),
    path("about/", about.about_page),
]
