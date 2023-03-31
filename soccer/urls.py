from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='soccer'),
    path('live/', views.live, name='live'),
    path('fixtures/<str:date>/', views.fixturesByDate, name='fixtures'),
    path('<str:country>/<str:league>/fixtures/', views.league_events, name='fixturesByleague'),
    path('<str:country>/<str:league>/results/', views.league_events, name='resultsByleague'),
    path('<str:country>/<str:league>/table/', views.league_events, name='tablesByleague'),
]
