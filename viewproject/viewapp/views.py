from django.shortcuts import render
from viewapp.models import viewtb

# Create your views here.

def greet(request):
    if request.method=='POST':
        obj=viewtb()
        obj.name=request.POST.get('name')
        obj.address=request.POST.get('address')
        obj.email=request.POST.get('email')
        obj.save()
    
    return render(request,'register.html')


def show(request):
    obj=viewtb.objects.all()
    return render(request,'views.html',{'data':obj})