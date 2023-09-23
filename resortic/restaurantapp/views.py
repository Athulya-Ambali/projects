from django.shortcuts import render
from restaurantapp.models import restb

# Create your views here.

def add(request):
    if request.method=='POST':
        obj=restb()
        obj.name=request.POST.get('name')
        obj.time=request.POST.get('time')
        obj.ctime=request.POST.get('ctime')
        obj.non=request.POST.get('non')
        obj.veg=request.POST.get('veg')
        obj.save()

    return render(request,'restaurant/restadd.html')

def vieww(request):
    obj=restb.objects.all()
    return render(request,'restaurant/restview.html',{'data':obj})


def up(request,pk):
    obj=restb.objects.get(re_id=pk)
    if request.method=='POST':
        obj=restb.objects.get(re_id=pk)
        obj.name=request.POST.get('name')
        obj.time=request.POST.get('time')
        obj.ctime=request.POST.get('ctime')
        obj.non=request.POST.get('non')
        obj.veg=request.POST.get('veg')
        obj.save()
    return render(request,'restaurant/restupdate.html',{'data':obj})

def delete(request,pk):
    obj=restb.objects.get(re_id=pk)
    obj.delete()
    return vieww(request)