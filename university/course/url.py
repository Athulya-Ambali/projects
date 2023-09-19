from django.urls import path
from course import views

urlpatterns = [
    path('',views.display),
    path('show/',views.show),
    
]
