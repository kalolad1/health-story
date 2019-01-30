from django.db import models


class AuthKey(models.Model):
    """An AuthKey functions as a password for a physician.

    Envision the possible scenario: when a medical student graduates with their
    degree, they are given an AuthKey by the American Medical Association. It
    could be any 8-30 digit alphanumeric code that is unique to them.

    When physicians log onto a patient's health story, they are required to
    enter their key as well. This provides a access log for a patient's profile,
    as well as limits platform access to only board certified physicians.

    Attributes:
        key: A string denoting the AuthKey.

    """
    key = models.CharField(max_length=30)

    def __str__(self):
        return self.key
