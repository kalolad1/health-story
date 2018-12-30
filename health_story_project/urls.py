from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Landing page
    path('', views.landing_page, name='landing-page'),

    # Account specific
    path('accounts/', include('accounts.urls'), name='accounts'),

    # Health Story specific
    path('health-story/', include('health_story.urls'), name='health_story')
]
