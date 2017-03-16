from django.shortcuts import render
from .models import Volunteer
from volunteers.models import Volunteer

def index(request):
    all_volunteers = Volunteer.objects.all()
    return render(request, 'volunteers/templates/volunteers/index.html', {'all_volunteers': all_volunteers})

def home(request):
    hello = "Hello World"
    return render(request, 'volunteers/templates/volunteers/index.html', {'all_volunteers': all_volunteers})
