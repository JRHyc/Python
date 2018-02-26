# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
from django.shortcuts import render, HttpResponse, redirect
  
def index(request):
    if not 'gold' in request.session:
        request.session['gold'] = 0
    if not 'message' in request.session:
        request.session['message']= ""
    
    return render(request, 'ninja_gold/index.html')


def process_money(request):
    if request.POST['building'] == 'farm':
        spin = random.randrange(10,21)
        result = "you earned {} farm gold".format(spin)
    elif request.POST['building'] == 'cave':
        spin = random.randrange(5,11)
        result = "you earned {} cave gold".format(spin)
    elif request.POST['building'] == 'house':
        spin = random.randrange(2,6)
        result = "you earned {} house gold".format(spin)
    elif request.POST['building'] == 'casino':
        spin = random.randrange(-50,51)
        if spin > 0:
            result = "you won {} gold!".format(spin)
        elif spin < 0:
            result = "you lost {} gold! :(".format(spin)
        elif spin == 0:
            result = "You broke even! At least you had fun!!"
    
    request.session['gold'] += spin
    request.session['message'] += result
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')
