from django.shortcuts import render
from course.models import *

# Create your views here.

def display(request):
    obj=Coursetb.objects.all()
    return render(request,'courseview.html',{'data':obj})   





def show(request):
    obj=Syllabustb.objects.all()
    return render(request,'syllabusview.html',{'data':obj})