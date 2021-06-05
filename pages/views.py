from django.shortcuts import render
from .models import Team


# Create your views here.

def home(request):
    teams = Team.objects.all()
    data_team = {
            'teams': teams,
    }
    return render(request, 'pages/home.html', data_team)


def about(request):
    teams = Team.objects.all()
    data_team = {
            'teams': teams,
        }
    return render(request, 'pages/about.html', data_team)


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    return render(request, 'pages/contact.html')
