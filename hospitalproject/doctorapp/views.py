from django.shortcuts import render
from doctorapp.models import doctortb

# Create your views here.

def greet(request):
    if request.method=='POST':
        obj=doctortb()
        obj.name=request.POST.get('name')
        obj.age=request.POST.get('age')
        obj.place=request.POST.get('place')
        obj.email=request.POST.get('email')
        obj.contact=request.POST.get('contact')
        obj.save()
    return render(request,'regidr.html')

def show(request):
    obj=doctortb.objects.all()
    return render(request,'views.html',{'data':obj})

def update(request,pk):
    obj=doctortb.objects.get(dr_id=pk)
    if request.method=='POST':
        obj=doctortb.objects.get(dr_id=pk)
        obj.name=request.POST.get('name')
        obj.age=request.POST.get('age')
        obj.place=request.POST.get('place')
        obj.email=request.POST.get('email')
        obj.contact=request.POST.get('contact')
        obj.save()
    return render(request,'updatedr.html',{'data':obj})

def delete(request,pk):
    obj=doctortb.objects.get(dr_id=pk)
    obj.delete()
    return show(request)