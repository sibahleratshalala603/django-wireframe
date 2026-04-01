from django.urls import path
from . import views

app_name = 'track'

urlpatterns = [
    path('', views.track_home, name='track_home'),
    path('log/', views.track_log, name='track_log'),
]
