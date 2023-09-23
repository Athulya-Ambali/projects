from django.urls import path
from secondapp import views

urlpatterns = [
    path('',views.sec),
    path('call/',views.call),
    
]