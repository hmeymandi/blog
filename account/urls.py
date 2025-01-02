from django.urls import path
from . import views



urlpatterns = [

    path ("singup" ,views.Singup_views.as_view(), name = "singup_views"),
   
]