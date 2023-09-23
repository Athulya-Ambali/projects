from django.shortcuts import render
from festivalapp.models import festtb

# Create your views here.

def add(request):
    if request.method=='POST':
        obj=festtb()
        obj.name=request.POST.get('name')
        obj.time=request.POST.get('time')
        obj.description=request.POST.get('description')
        obj.save()

    return render(request,'festival/festadd.html')

def vieww(request):
    obj=festtb.objects.all()
    return render(request,'festival/festview.html',{'data':obj})

def update(request,pk):
    obj=festtb.objects.get(fest_id=pk)
    if request.method=='POST':
        obj=festtb.objects.get(fest_id=pk)
        obj.name=request.POST.get('name')
        obj.time=request.POST.get('time')
        obj.description=request.POST.get('description')
        obj.save()
    return render(request,'festival/festupdate.html',{'data':obj})

def delete(request,pk):
    obj=festtb.objects.get(fest_id=pk)
    obj.delete()
    return vieww(request)