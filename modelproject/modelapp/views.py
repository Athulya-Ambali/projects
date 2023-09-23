from django.shortcuts import render
from modelapp.models import modetb


# Create your views here.

def greet(request):
    if request.method=='POST':
        obj=modetb()
        obj.name=request.POST.get('name')
        obj.address=request.POST.get('address')
        obj.email=request.POST.get('email')
        obj.save()
    return render(request,'web.html')
