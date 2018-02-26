# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
  
def index(request):
    response = "Hello, I am in your surveys app!"
    return HttpResponse(response)

def new(request):
    response = "Hello, this is where you will create a new survey"
    return HttpResponse(response)

# Create your views here.
