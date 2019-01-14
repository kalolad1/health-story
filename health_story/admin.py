from django.contrib import admin
from .models import Patient, HealthEncounter, Relative, Disease

# Register your models here.
admin.site.register(Patient)
admin.site.register(HealthEncounter)
admin.site.register(Relative)
admin.site.register(Disease)

