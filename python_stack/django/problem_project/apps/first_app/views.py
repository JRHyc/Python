# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "Hello, I am your first request from the blogs app!"
    return HttpResponse(response)

def new(request):
    response = "Hello, this is the new page"
    return HttpResponse(response)

def create(request):
    response = "Hello, this is the create page"
    return redirect('/')

def show(request, number):
    response = "Hello, this is a place holder for blog number {}".format(number)
    return HttpResponse(response)

def edit(request, number):
    response = "Hello, this is a place holder for editing blog number {}".format(number)
    return HttpResponse(response)

def delete(request, number):
    response = "Hello, this is a place holder for deleting blog number {}".format(number)
    return redirect('/')


# Create your views here.
