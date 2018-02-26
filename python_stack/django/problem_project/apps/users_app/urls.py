from django.conf.urls import url
from . import views           # This line is new!
   
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^users$', views.users),
    url(r'^new$', views.new),      # This line has changed!
]