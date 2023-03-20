from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.add_blog, name='add_post'),
    path('edit/', views.blog_update, name='edit_post'),
    path('detail/<str:slug>/', views.blog_detail, name='blog_detail'),
    path('delete/<str:slug>/', views.blog_delete, name='delete_post'),
]