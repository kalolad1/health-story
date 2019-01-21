from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login_page, name='accounts/login'),
    path('login-patient/', views.login_patient, name='accounts/login-patient'),
    path('login-physician/', views.login_physician, name='accounts/login-physician'),

    path('sign-up/', views.sign_up, name='accounts/sign-up'),
    path('logout/', views.logout, name='accounts/logout'),
    path('patient-registration/', views.patient_registration, name='accounts/patient-registration'),
]
