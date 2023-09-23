from django.urls import path
from exm2app import views

urlpatterns = [
    path('',views.greet),
   
]

