from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sec(request):
    return HttpResponse("<h1>the second app</h1>")

def call(request):
    return HttpResponse("<h1>call the app</h1>")