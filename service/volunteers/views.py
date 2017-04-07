from django.shortcuts import render
from .models import Volunteer
from volunteers.models import Volunteer, VolunteerHours
from volunteers.forms import VolunteerForm

def index(request):
    context = {}
    return render(request, 'volunteers/index.html', context)

def detail(request):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        vf = VolunteerForm
        hours = VolunteerHours.objects.filter(user=request.user)
        context = {'vf': vf, 'hours': hours}
    return render(request, 'volunteers/detail.html', context)

#def home(request):
#    hello = "Hello World"
#    return render(request, 'home.html', {'all_volunteers': all_volunteers})
