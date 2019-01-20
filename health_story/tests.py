from django.test import TestCase
from .models import Patient
from datetime import date, datetime


class PatientTestCase(TestCase):
    def setUp(self):
        Patient.objects.create(first_name="Rishi", last_name="Konkesa",
                               username="rishinator", date_of_birth=date.min)

    def test_patients_physician_code_VALID(self):
        patient = Patient.objects.get(username="rishinator")
        patient.physician_code = "TESTCODE"
        patient.physician_code_created = datetime.now()
        self.assertEquals(patient.is_physician_code_valid("TESTCODE"), True)

        patient.physician_code = "TESTCODE1"
        self.assertEquals(patient.is_physician_code_valid("TESTCODE"), False)

        patient.physician_code = "TESTCODE"
        patient.physician_code_created = datetime(year=2040, month=12, day=1)
        self.assertEquals(patient.is_physician_code_valid("TESTCODE"), False)
