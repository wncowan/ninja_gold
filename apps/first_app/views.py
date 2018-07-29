# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
# from django.utils.crypto import get_random_string
from random import *
from time import gmtime, strftime

# Create your views here.
def index(request):
    if 'activities' not in request.session:
        request.session['activities'] = []
    if 'gold' not in request.session:
        request.session['gold'] = 0
    return render(request, 'first_app/index.html')

def process(request, place):
    print place
    if request.method == "POST":
        if place == "farm":
            plunder = randint(10,20)
            request.session['gold'] += plunder
            request.session['activities'].append("plundered {} from {} at {}".format(plunder, place, strftime("%Y-%m-%d %H:%M %p", gmtime())))
            return redirect('/')
        elif place == "cave":
            plunder = randint(5,10)
            request.session['gold'] += plunder
            request.session['activities'].append("plundered {} from {} at {}".format(plunder, place, strftime("%Y-%m-%d %H:%M %p", gmtime())))
            return redirect('/')
        elif place == "house":
            plunder = randint(2,5)
            request.session['gold'] += plunder
            request.session['activities'].append("plundered {} from {} at {}".format(plunder, place, strftime("%Y-%m-%d %H:%M %p", gmtime())))
            return redirect('/')
        elif place == "casino":
            plunder = randint(-50,50)
            if plunder < 0:
                result = "wasted"
            else: 
                result = "won"
            request.session['gold'] += plunder
            request.session['activities'].append("{} {} from {} at {}".format(result, plunder, place, strftime("%Y-%m-%d %H:%M %p", gmtime())))
            return redirect('/')
        # request.session['count'] += 1
        # request.session['name'] = request.POST['name']
        # request.session['location'] = request.POST['location']
        # request.session['language'] = request.POST['language']
        # request.session['comment'] = request.POST['comment']
    return redirect('/')

def reset(request):
    del request.session['activities']
    return redirect('/')