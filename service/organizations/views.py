from django.shortcuts import render
from django.http import HttpResponse
from organizations.models import Organization

def index(request):
    return render(request, 'organizations/index.html', context)
