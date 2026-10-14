
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("certifications/", views.certifications, name="certifications"),
    path("projects/", views.projects, name="projects"),
    path("contacts/", views.contacts, name="contacts"),
]
