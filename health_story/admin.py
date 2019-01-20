from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Patient)
admin.site.register(models.HealthEncounter)
admin.site.register(models.Relative)
admin.site.register(models.Medication)
admin.site.register(models.Condition)


