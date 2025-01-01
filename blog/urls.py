from django.urls import path
from . import views



urlpatterns = [

    path ("" , views.PostListView.as_view(), name = "post_listview"),
    path("<int:pk>/",views.Post_detail_view.as_view(),name = "post_detail_view"),
    path("create/",views.Create_PostView.as_view(),name = "create_post"),
    path("<int:pk>/update",views.Update_PostView.as_view(),name = "post_detail_update"),
    path('<int:pk>/delete', views.Delete_PostView.as_view(), name='post_delete'),
]