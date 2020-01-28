from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='movies-home'),
    path('info/', views.info, name='movies-info'),
]