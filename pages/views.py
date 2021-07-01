from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def about_view(request, *args, **kwargs):
    prince = {
        'name': "Prince ELdrige",
        'age': 20,
        'achievements': ['hey', 'there', 'from', 'apoh', 'prince']
    }
    return render(request, "about.html", prince)
