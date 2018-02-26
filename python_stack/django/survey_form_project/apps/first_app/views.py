# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    if not 'count' in request.session:
        request.session['count'] = 0
        print request.session['count']


    return render(request, 'first_app/index.html')

def process(request):
    request.session['name'] = request.POST['name']
    request.session['dojo_location'] = request.POST['dojo_location']
    request.session['favorite_language'] = request.POST['favorite_language']
    request.session['comment'] = request.POST['comment']
    request.session['count'] += 1

    print request.session['name']
    print request.session['dojo_location']
    print request.session['favorite_language']
    print request.session['comment']


    return redirect('/result')

def result(request):

    return render(request,'first_app/result.html')

def refresh(request):
    print "I'm working!"
    return redirect('/')