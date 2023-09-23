from django.urls import path
from resortapp import views

urlpatterns = [
    path('',views.add),
    path('vot/',views.vieww),
    path('update/(?P<pk>\w+)',views.update,name="update"),
    path('delete/(?P<pk>\w+)',views.delete,name="delete"),
   
]

