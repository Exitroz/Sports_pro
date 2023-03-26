from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='soccer'),
    path('live/', views.live, name='live'),
    path('fixtures/<str:date>/', views.fixturesByDate, name='fixtures')
]
