from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
    url(r'^$', views.index),
    url(r'^users/$', views.index),
    url(r'^users/new/$', views.new),
    url(r'^new$', views.new),
    url(r'^process$', views.process),
    url(r'^show/(?P<number>\d+)$', views.show),
    url(r'^destroy/(?P<number>\d+)$', views.destroy),
    url(r'^edit/(?P<number>\d+)$', views.edit),
    url(r'^users/(?P<number>\d+)/update$', views.update),
    url(r'^(?P<number>\d+)/update$', views.update),
    url(r'^edit/(?P<number>\d+)/update$', views.update),
    url(r'^(?P<number>\d+)/edit$', views.edit),    # This line has changed!
]