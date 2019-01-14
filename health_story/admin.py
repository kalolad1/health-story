from django.contrib import admin
from .models import Patient, HealthEncounter

# Register your models here.
admin.site.register(Patient)
admin.site.register(HealthEncounter)