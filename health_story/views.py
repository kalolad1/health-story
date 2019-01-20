from django.shortcuts import render, redirect
from .models import Patient, HealthEncounter
from django.contrib.auth.decorators import login_required
from django.core import serializers
from datetime import datetime
from .helper.constants import MPConstants, PAConstants
import random
import string


@login_required
def set_up(request):
    """Caches important patient information using cookies.

    This function is called each time user enters a new session.
    It is used to store cookies to prevent unnecessary database queries.
    """
    patient = Patient.objects.get(username=request.user.username)
    info = patient.get_all_patient_info()

    request.session[PAConstants.PATIENT_ID] = patient.id
    request.session[MPConstants.MEDICATIONS] = serializers.serialize('json', info[MPConstants.MEDICATIONS])
    request.session[MPConstants.CONDITIONS] = serializers.serialize('json', info[MPConstants.CONDITIONS])
    return redirect('health_story/demographics')


# Main pages.
@login_required
def demographics(request):
    patient = Patient.objects.get(id=request.session[PAConstants.PATIENT_ID])
    return render(request, 'health_story/demographics.html', {'patient': patient})


@login_required
def vitals(request):
    patient = Patient.objects.get(id=request.session[PAConstants.PATIENT_ID])
    return render(request, 'health_story/vitals.html', {'patient': patient})


@login_required
def timeline(request):
    patient = Patient.objects.get(id=request.session[PAConstants.PATIENT_ID])
    health_encounters = HealthEncounter.objects.filter(patient=patient)

    return render(request, 'health_story/timeline.html', {'patient': patient,
                                                          'health_encounters': health_encounters})


@login_required
def family_history(request):
    patient = Patient.objects.get(id=request.session[PAConstants.PATIENT_ID])
    relatives = patient.relatives.all()

    return render(request, 'health_story/family-history.html', {'patient': patient,
                                                                'relatives': relatives})


@login_required
def medications(request):
    patient = Patient.objects.get(id=request.session[PAConstants.PATIENT_ID])

    deserialized_objects = serializers.deserialize('json', request.session[MPConstants.MEDICATIONS])
    medications = [medications.object for medications in deserialized_objects]

    return render(request, 'health_story/medications.html',
                  {'patient': patient, MPConstants.MEDICATIONS: medications})


@login_required
def conditions(request):
    patient = Patient.objects.get(id=request.session[PAConstants.PATIENT_ID])

    deserialized_objects = serializers.deserialize('json', request.session[MPConstants.CONDITIONS])
    conditions = [conditions.object for conditions in deserialized_objects]

    return render(request, 'health_story/conditions.html',
                  {'patient': patient, MPConstants.CONDITIONS: conditions})


@login_required
def generate_physician_key(request):
    """Generates a random 8 digit code for the physician to enter.
    The code expires within an hour of creation. A alphanumeric 8
    digit code has 2.8211099e+12 combinations and is extremely robust
    against brute force hacking attempts.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse object displaying code to the user.
    """
    code_length = 8
    patient = Patient.objects.get(id=request.session[PAConstants.PATIENT_ID])
    patient.physician_code = ''.join(random.choices(string.ascii_letters + string.digits, k=code_length))
    patient.physician_code_created = datetime.now()

    return render(request, 'health_story/secondary/generate-physician-key.html',
                  {'patient': patient})




