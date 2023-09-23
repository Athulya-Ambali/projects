from django.urls import path
from vazhipaduapp import views

urlpatterns = [
    path('',views.add),
    path('vvazh/',views.vvazh),
    path('update/(?P<pk>\w+)',views.vup,name="upd"),
    path('delete/(?P<pk>\w+)',views.delete,name="del"),
   
]
