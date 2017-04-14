from django.shortcuts import render
from django.http import HttpResponse
from organizations.models import Organization

def detail(request):
    all_organizations = Organization.objects.filter(active=True).order_by('entered')
    context = {'all_organizations': all_organizations}
    return render(request, 'organizations/index.html', context)
