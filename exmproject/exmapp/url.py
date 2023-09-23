from django.urls import path
from exmapp import views

urlpatterns = [
    path('',views.greet),
    path('show/',views.show),
    path('display/',views.display),
]
