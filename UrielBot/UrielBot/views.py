from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from datetime import datetime



def index (request):
    message = 'accueil'

    return HttpResponse(message)