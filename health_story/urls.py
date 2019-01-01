from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='health_story/home'),
    path('timeline/', views.timeline, name='health_story/timeline'),

]
