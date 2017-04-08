from django.shortcuts import render
from .models import Volunteer
from volunteers.models import Volunteer, VolunteerHours
from volunteers.forms import VolunteerForm

def index(request):
    context = {}
    return render(request, 'volunteers/index.html', context)

def detail(request):
    if not request.user.is_authenticated:
        context = {}
    else:
        if request.method == "POST":
            form = VolunteerForm(request.POST)
            if form.is_valid():
                recorded_hours = form.save(commit=false)
                recorded_hours.user = request.user
                recorded_hours.save()
                return redirect('/volunteers/')
            else:
                pass
            return render_to_response('web/animal_form.html', variables)
        else:
            form = VolunteerForm
            hours = VolunteerHours.objects.filter(user=request.user)
            context = {'form': form, 'hours': hours}
    return render(request, 'volunteers/detail.html', context)
