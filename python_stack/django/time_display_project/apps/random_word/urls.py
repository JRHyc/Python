from django.conf.urls import url
from . import views           # This line is new!


urlpatterns = [
    url(r'^$', views.random),
    url(r'^random_word$', views.random),
    url(r'^generate$', views.generate),
    url(r'^random_word/random.html$', views.random),
    url(r'^reset$', views.reset)     # This line has changed!
]