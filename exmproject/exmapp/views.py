from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def greet(request):
    return HttpResponse("<h1>hello welcome to home page</h1>")

def show(request):
    return HttpResponse("<h2>hii this is your contact page</h2>")

def display(request):
    return HttpResponse("<p>here is your contact details</p>")