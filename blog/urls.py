from django.urls import path

from . import views

urlpatterns = [
    path('add-post/', views.add_blog, name='add_post'),
    path('edit-post/', views.blog_update, name='edit_post'),
    path('blog-detail/<str:slug>/', views.blog_detail, name='blog_detail'),
    path('delete-post/', views.blog_delete, name='delete_post'),
]