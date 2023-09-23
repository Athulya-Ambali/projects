from django.shortcuts import render



# Create your views here.

def greet(request):
    return render(request,'templ.html')

def home(request):
    return render(request,'home.html',{'name':'ONETEAMSOLUTIONS'})