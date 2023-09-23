
from django.urls import path
from tplapp import views

urlpatterns = [
    path('',views.greet),
    path('home/',views.home)
]
