from django.conf.urls import url
from . import views

urlpatterns = [
    # /volunteers/
    url(r'^$', views.index, name= 'index'),

]
