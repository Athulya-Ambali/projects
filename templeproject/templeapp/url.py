from django.urls import path
from templeapp import views

urlpatterns = [
   
    path('',views.add),
    path('vtem/',views.vtem),
    path('upd/(?P<pk>\w+)',views.update,name="update"),
    path('del/(?P<pk>\w+)',views.delete,name="delete"),
]

