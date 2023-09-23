from django.urls import path
from restaurantapp import views

urlpatterns = [
    
    path('',views.add),
    path('vres/',views.vieww),
    path('up/(?P<pk>\w+)',views.up,name="up"),
    path('delete/(?P<pk>\w+)',views.delete,name="delete"),
    
]