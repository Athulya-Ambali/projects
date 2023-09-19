from django.urls import path
from doctorapp import views

urlpatterns = [
    
    path('',views.greet),
    path('show/',views.show),
    path('update/(?P<pk>\w+)',views.update,name="update"),
    path('delete/(?P<pk>\w+)',views.delete,name="delete")
    
]


