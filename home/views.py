
from django.shortcuts import render

from home.models import Car

def home_view(request):
    context = {
        'site_name': 'Cars',
        'cars': Car.objects.all()
    }
    return render(request, "home/home.html", context)

def pepsi_view(request):
    context = {
        'site_name': 'Cars',
        'cars': Car.objects.all()
    }
    return render(request, "home/pepsi.html", context)

