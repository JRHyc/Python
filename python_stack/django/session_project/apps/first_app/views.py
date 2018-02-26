# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if not 'add_word' in request.session:
        request.session['word'] = "test"
    if not 'color' in request.session:
        request.session['color'] = "test"
    if not 'phat' in request.session:
        request.session['phat'] = 
    return render(request, "first_app/index.html")

def word(request):
    request.session['add_word'] = request.POST['add_word']
    request.session['color'] = request.POST['color']
    request.session['phat'] = request.POST['phat']

    print request.session['add_word']
    print request.session['color']
    print request.session['phat']

    return redirect('/')