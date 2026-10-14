
from django.shortcuts import render


def home(request):
    return render(request, "portfolio/index.html")


def about(request):
    return render(request, "portfolio/about.html")


def certifications(request):
    return render(request, "portfolio/certifications.html")


def projects(request):
    return render(request, "portfolio/projects.html")


def contacts(request):
    return render(request, "portfolio/contacts.html")
