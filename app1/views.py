from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def firstapp(requuest):
    return HttpResponse('<h1>first app Details</h1>')