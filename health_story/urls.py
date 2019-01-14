from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='health_story/home'),

    # Main pages.
    path('demographics/', views.demographics, name='health_story/demographics'),
    path('vitals/', views.vitals, name='health_story/vitals'),
    path('timeline/', views.timeline, name='health_story/timeline'),

    # Add/modify pages.
    path('add-health-encounter/', views.add_health_encounter, name='health_story/modify/add_health_encounter'),
]
