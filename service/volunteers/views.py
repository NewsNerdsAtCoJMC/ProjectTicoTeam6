from django.shortcuts import render
from .models import Volunteer
# Create your views here.
def index(request):
    all_volunteers = Volunteer.objects.all()
    return render(request, 'volunteers/index.html', {'all_volunteers': all_volunteers})
