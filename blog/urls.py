from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostView.as_view(), name='posts_view'),
    path('detail/<int:pk>/', views.DetailView.as_view(), name='detail_view'),
    path('create_post/', views.CreatePost.as_view(), name='create_post'),
    path('edit_post/<int:pk>', views.EditPost.as_view(), name='edit_post'),
    path('del_post/<int:pk>', views.del_post, name='del_post'),
    
]
