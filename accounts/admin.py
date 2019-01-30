from django.contrib import admin

from . import models

# Register models for the admin console at http://<your.server.path>/admin
admin.site.register(models.AuthKey)
