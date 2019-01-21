from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.set_up, name='health_story/set_up'),

    # Main pages.
    path('demographics/', views.demographics, name='health_story/demographics'),
    path('vitals/', views.vitals, name='health_story/vitals'),
    path('timeline/', views.timeline, name='health_story/timeline'),
    path('family-history/', views.family_history, name='health_story/family_history'),
    path('medications/', views.display_medications, name='health_story/medications'),
    path('conditions/', views.display_conditions, name='health_story/conditions'),

    # Generate physician key
    path('generate-physician-key/', views.generate_physician_key,
         name='health_story/generate_physician_key'),

    # Edit patient info
    path('edit-patient-info/', views.edit_patient_info, name='health_story/edit_patient_info'),
    path('add-health-encounter/', views.add_health_encounter, name='health_story/add_health_encounter'),
    path('add-family-history/', views.add_family_history, name='health_story/add_family_history'),

]
