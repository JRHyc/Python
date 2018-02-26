# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
  
def index(request):
    response = "Hello, I am from the users app!"
    return HttpResponse(response)

def register(request):
    response = "This is where we will create new users. This is the register page"
    return HttpResponse(response)

def login(request):
    response = "This is where users will be able to login!"
    return HttpResponse(response)

def users(request):
    response = "This is where we will display a list of all users"
    return HttpResponse(response)

def new(request):
    return redirect('/register')


