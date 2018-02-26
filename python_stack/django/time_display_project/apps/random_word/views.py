# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


# Create your views here.
def random(request):
    context = {
        'word': get_random_string(14)
    }
    if not 'count' in request.session:
        request.session['count'] = 5
        print request.session['count']
    
    return render(request, "random_word/random.html", context)

def generate(request):
    request.session['count'] += 1
    print request.session['count']

    return redirect("random_word/random.html")

def reset(request):
    request.session['count'] = 0
    print request.session['count']

    return redirect("random_word/random.html")