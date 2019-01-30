from django.urls import path
from . import views

# Example flow of an user
# 1. Sign up for an account
# 2. Go through Patient Registration. This is where they fill out
#    demographic and other information.
# 3. Enter their health story view (this is the main screen once logged in)
# 4. Logout and get redirected to the landing page.

urlpatterns = [
    # Paths to login.
    path('login/', views.login_page, name='accounts/login'),
    path('login-patient/', views.login_patient, name='accounts/login-patient'),
    path('login-physician/', views.login_physician,
         name='accounts/login-physician'),

    # Path to sign up
    path('sign-up/', views.sign_up, name='accounts/sign-up'),

    # Path to logout. This does not render a HttpResponse, it redirects
    # back to the landing page.
    path('logout/', views.logout, name='accounts/logout'),

    # Path to the patient registration page.
    path('patient-registration/', views.patient_registration,
         name='accounts/patient-registration'),
]
