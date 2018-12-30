from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login, name='accounts/login'),
    path('sign-up/', views.sign_up, name='accounts/sign-up'),
    path('logout/', views.logout, name='accounts/logout'),
]
