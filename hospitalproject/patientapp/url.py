from django.urls import path
from patientapp import views

urlpatterns = [
    
    path('display/',views.display),
    path('like/',views.like),
    path('update/(?P<pk>\w+)',views.update,name="update"),
    path('delete/(?P<pk>\w+)',views.delete,name="delete")
    
]
