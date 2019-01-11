from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='health_story/home'),
    path('timeline/', views.timeline, name='health_story/timeline'),

    path('demographics/', views.demographics, name='health_story/demographics'),
    path('vitals/', views.vitals, name='health_story/vitals'),
]
