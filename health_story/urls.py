from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.demographics, name='health_story/home'),

    # Main pages.
    path('demographics/', views.demographics, name='health_story/demographics'),
    path('vitals/', views.vitals, name='health_story/vitals'),
    path('timeline/', views.timeline, name='health_story/timeline'),
    path('family-history/', views.family_history, name='health_story/family_history'),
    path('medications/', views.medications, name='health_story/medications'),
    path('conditions/', views.conditions, name='health_story/conditions'),

    # Generate physician key
    path('generate-physician-key', views.generate_physician_key,
         name='health_story/generate_physician_key')



]
