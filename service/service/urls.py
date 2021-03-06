"""service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from volunteers import views as volunteer_views
from organizations import views as organizations_views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    url(r'^$', volunteer_views.index, name='index'),
    url(r'^volunteers/$', volunteer_views.detail, name='index'),
    url(r'^organizations/$', organizations_views.detail, name='index'),
    url(r'^about/$', volunteer_views.about, name='index'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', admin.site.urls),
    #url(r'^organizations/', organizations_views.home, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
