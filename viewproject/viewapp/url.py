from django.urls import path
from viewapp import views

urlpatterns = [

    path('',views.greet),
    path('show/',views.show)

]
