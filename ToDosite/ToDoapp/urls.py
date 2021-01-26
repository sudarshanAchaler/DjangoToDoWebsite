from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home' ),
    path('CreateTask/', views.createTask, name='createTask'),
    path('UpdateTask/', views.updateTask, name='updateTask'),
    
]
