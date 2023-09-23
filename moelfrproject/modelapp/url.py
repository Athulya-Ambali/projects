from django.urls import path
from modelapp import views

urlpatterns = [
    path('',views.index,name="home"),
    path('add/',views.addcustomer)
]

