from django.shortcuts import render
from resortapp.models import resortb

# Create your views here.

def add(request):
    if request.method=='POST':
        obj=resortb()
        obj.name=request.POST.get('name')
        obj.email=request.POST.get('email')
        obj.contact=request.POST.get('contact')
        obj.rooms=request.POST.get('rooms')
        obj.single=request.POST.get('single')
        obj.double=request.POST.get('double')
        obj.family=request.POST.get('family')
        obj.sprice=request.POST.get('sprice')
        obj.dprice=request.POST.get('dprice')
        obj.fprice=request.POST.get('fprice')
        obj.price=request.POST.get('price')
        obj.save()
    
    return render(request,'resort/resortadd.html')

def vieww(request):
    obj=resortb.objects.all()
    return render(request,'resort/resortview.html',{'data':obj})

def update(request,pk):
    obj=resortb.objects.get(ro_id=pk)
    if request.method=='POST':
        obj=resortb.objects.get(ro_id=pk)
        obj.name=request.POST.get('name')
        obj.email=request.POST.get('email')
        obj.contact=request.POST.get('contact')
        obj.rooms=request.POST.get('rooms')
        obj.single=request.POST.get('single')
        obj.doble=request.POST.get('double')
        obj.family=request.POST.get('family')
        obj.sprice=request.POST.get('sprice')
        obj.dprice=request.POST.get('dprice')
        obj.fprice=request.POST.get('fprice')
        obj.price=request.POST.get('price')
        obj.save()
    return render(request,'resort/resortupdate.html',{'data':obj})

def delete(request,pk):
    obj=resortb.objects.get(ro_id=pk)
    obj.delete()
    return vieww(request)