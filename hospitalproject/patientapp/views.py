from django.shortcuts import render
from patientapp.models import patientb

# Create your views here.

def display(request):
    if request.method=='POST':
        obj=patientb()
        obj.name=request.POST.get('name')
        obj.address=request.POST.get('address')
        obj.date=request.POST.get('date')
        obj.department=request.POST.get('department')
        obj.disease=request.POST.get('disease')
        obj.save()
    return render(request,'bookpa.html')

def like(request):
    obj=patientb.objects.all()
    return render(request,'viewpa.html',{'data':obj})

def update(request,pk):
    obj=patientb.objects.get(pa_id=pk)
    if request.method=="POST":
        obj=patientb.objects.get(pa_id=pk)
        obj.name=request.POST.get('name')
        obj.address=request.POST.get('address')
        obj.date=request.POST.get('date')
        obj.department=request.POST.get('department')
        obj.disease=request.POST.get('disease')
        obj.save()
    return render(request,'updatepa.html',{'data':obj})

def delete(request,pk):
    obj=patientb.objects.get(pa_id=pk)
    obj.delete()
    return like(request)
