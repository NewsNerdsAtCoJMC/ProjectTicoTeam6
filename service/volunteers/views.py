from django.shortcuts import render
<<<<<<< HEAD
from .models import VolunteerConfig
# Create your views here.
def index(request):
    all_volunteers = volunteers.objects.all()
    return render(request, 'volunteers/templates/volunteers/index.html', {'all_volunteers': all_volunteers})

def home(request):
    hello = "Hello World"
    return render(request, 'volunteers/templates/volunteers/index.html', {'all_volunteers': all_volunteers})
=======
from django.http import HttpResponse
from volunteers.models import Volunteer

def index(request):
    return render(request, 'organizations/index.html', context)
>>>>>>> origin/master
