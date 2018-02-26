# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from .models import *
from django.contrib import messages
  
def index(request):
    context = {}
    context['search'] = User.objects.all()
    return render(request, 'restful_users_app/index.html',context)

def new(request):
    
    return render(request, 'restful_users_app/new.html')

def process(request):
    first = request.POST['first']
    last = request.POST['last']
    email = request.POST['email']

    x = {'first_name':first, 'last_name':last, 'email':email}
    errors = User.objects.validate(x)
    if errors:
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
            return redirect('/new')
    else:
        user = User.objects.create(first_name = first, last_name = last, email = email)
        print User.objects.all()
    
        return redirect('/')

def show(request, number):
    context = {}
    context['info'] = User.objects.get(id = number)

    return render(request, 'restful_users_app/users.html', context)

def destroy(request, number):
    j = User.objects.get(id=number)
    print j
    j.delete()

    return redirect('/')

def edit(request, number):
    context = {}
    context['info'] = User.objects.get(id = number)

    return render(request, 'restful_users_app/edit.html', context)

def update(request, number):
    first = request.POST['first']
    last = request.POST['last']
    email = request.POST['email']

    x = {'first_name':first, 'last_name':last, 'email':email}
    errors = User.objects.validate(x)
    if errors:
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
            return redirect("/edit/{}".format(number))
    else:
        user = User.objects.get(id = number)
        user.first_name = request.POST['first']
        user.last_name = request.POST['last']
        user.email = request.POST['email']
        user.save()

    return redirect('/')
