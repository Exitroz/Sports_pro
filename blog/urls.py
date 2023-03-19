from django.urls import path

from . import views

urlpatterns = [
    path('add-post/', views.add_blog, name='add_post')
]