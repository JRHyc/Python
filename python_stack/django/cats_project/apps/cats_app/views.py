# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    print "hooray!!!"
    return render(request, "cats_app/index.html")

def new(request):
    return render(request, "cats_app/new.html")

