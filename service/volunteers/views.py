from django.shortcuts import render
from django.http import HttpResponse
from volunteers.models import Volunteer

def index(request):
    return render(request, 'organizations/index.html', context)
