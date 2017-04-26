from django.shortcuts import render
from .models import Volunteer
from volunteers.models import Volunteer, VolunteerHours
from volunteers.forms import VolunteerForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def index(request):
    context = {}
    return render(request, 'volunteers/index.html', context)

@login_required(login_url='/accounts/login/')
def detail(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            recorded_hours = form.save(commit=False)
            recorded_hours.user = request.user
            recorded_hours.save()
            return redirect('/volunteers/')
    else:
        form = VolunteerForm()
        hours = VolunteerHours.objects.filter(user=request.user)
        context = {'form': form, 'hours': hours}
        return render(request, 'volunteers/detail.html', context)

def about(request):
        about = {}
        return render(request, 'volunteers/about.html', about)
