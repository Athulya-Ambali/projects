from django.shortcuts import render
from vazhipaduapp.models import vazhitb

# Create your views here.

def add(request):
    if request.method=='POST':
        obj=vazhitb()
        obj.name=request.POST.get('name')
        obj.price=request.POST.get('price')
        obj.save()

    return render(request,'vazhipadu/vazhiadd.html')

def vvazh(request):
    obj=vazhitb.objects.all()
    return render(request,'vazhipadu/vazhiview.html',{'data':obj})

def vup(request,pk):
    obj=vazhitb.objects.get(vazhi_id=pk)
    if request.method=='POST':
        obj=vazhitb.objects.get(vazhi_id=pk)
        obj.name=request.POST.get('name')
        obj.price=request.POST.get('price')
        obj.save()
    return render(request,'vazhipadu/vazhiupdate.html',{'data':obj})

def delete(request,pk):
    obj=vazhitb.objects.get(vazhi_id=pk)
    obj.delete()
    return vvazh(request)

