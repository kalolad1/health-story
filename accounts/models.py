from django.db import models


class AuthKey(models.Model):
    key = models.CharField(max_length=30)

    def __str__(self):
        return self.key
