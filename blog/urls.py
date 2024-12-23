from django.urls import path
from . import views



urlpatterns = [

    path ("" , views.post_listview, name = "post_listview"),

]