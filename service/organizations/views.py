from django.shortcuts import render
from django.http import HttpResponse
from organizations.models import Organization

def index(request):
    all_organizations = Organization.objects.all()
    return render(request, 'organizations/index.html', context)
def home(request):
    hello = "Hello World"
    return render(request, 'organizations/templates/organizations/index.html', {'all_organizations': all_organizations})
