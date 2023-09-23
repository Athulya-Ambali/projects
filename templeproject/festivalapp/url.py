from django.urls import path
from festivalapp import views

urlpatterns = [
    
    path('',views.add),
    path('vieww/',views.vieww),
    path('update/(?P<pk>\w+)',views.update,name="update"),
    path('delete/(?P<pk>\w+)',views.delete,name="delete"),

]
