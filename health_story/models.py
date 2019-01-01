from django.db import models
from datetime import date
from django.utils import timezone


class Patient(models.Model):
    # Demographic information
    # The following fields are required to filled out by the user.
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    email = models.CharField(max_length=75)
    sex = models.CharField(max_length=50)
    race = models.CharField(max_length=50)

    # The following fields are calculated without user input.
    date_created = models.DateField(default=timezone.now)

    def __str__(self):
        """Returns the string representation of the patient object.

        Returns:
            string: Full name of the patient.
        """
        return self.full_name()

    def full_name(self):
        """Returns the full name of the patient.

        Returns:
            string: The full name of the patient.
        """
        return self.first_name + " " + self.last_name

    def get_age(self):
        """Calculates the age of the patient based on their date of birth.

        Returns:
            int: The age of the patient.
        """
        days_old = (date.today() - self.date_of_birth).days
        return days_old // 365

    def date_of_first_visit_formatted(self):
        """Formats the date of the patients first visit in a readable way.

        Returns:
            string: The date of the first visit.
        """
        return self.date_created.strftime("%b %e %Y'")

    @staticmethod
    def is_user_registered(username):
        try:
            Patient.objects.get(username=username)
            return True
        except Patient.DoesNotExist:
            return False
