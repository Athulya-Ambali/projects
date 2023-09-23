from django.shortcuts import render
from django.http import HttpResponse
from modelapp.models import customer
from modelapp.forms import customerform

# Create your views here.

def index(request):
    custform=customerform()
    return render(request,"index.html",{"form":custform})

def addcustomer(request):
    try:
        if request.method=="POST":
            custform=customerform(request.POST)
            if custform.is_valid():
                custform.save()
        return render(request,'index.html',{"form":custform,"msg":"customer added"})
    except Exception as e:
        print(e)
        return HttpResponse("error")
    
