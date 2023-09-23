from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def display(request):
   return HttpResponse("<h1>hello world</h1>")

def greet(request):
   return HttpResponse("<h1>hey haiiii</h1>")