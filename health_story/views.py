from django.shortcuts import render
from .models import Patient, HealthEncounter
from django.contrib.auth.decorators import login_required
from datetime import datetime
import random
import string


# Main pages.
@login_required
def demographics(request):
    # Sets the patient_id to be used on every other page.
    # TODO store actually patient object, if possible, not id, to avoid
    # TODO redundant queries.
    patient = Patient.objects.get(username=request.user.username)
    request.session['patient_id'] = patient.id

    return render(request, 'health_story/demographics.html', {'patient': patient})


@login_required
def vitals(request):
    patient = Patient.objects.get(id=request.session['patient_id'])
    return render(request, 'health_story/vitals.html', {'patient': patient})


@login_required
def timeline(request):
    patient = Patient.objects.get(id=request.session['patient_id'])
    health_encounters = HealthEncounter.objects.filter(patient=patient)

    return render(request, 'health_story/timeline.html', {'patient': patient,
                                                          'health_encounters': health_encounters})


@login_required
def family_history(request):
    patient = Patient.objects.get(id=request.session['patient_id'])
    relatives = patient.relatives.all()

    return render(request, 'health_story/family-history.html', {'patient': patient,
                                                                'relatives': relatives})


@login_required
def medications(request):
    patient = Patient.objects.get(id=request.session['patient_id'])
    medications = patient.medications.all()
    return render(request, 'health_story/medications.html', {'patient': patient,
                                                             'medications': medications})


@login_required
def conditions(request):
    patient = Patient.objects.get(id=request.session['patient_id'])
    conditions = patient.conditions.all()
    return render(request, 'health_story/conditions.html', {'patient': patient,
                                                             'conditions': conditions})


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
    patient = Patient.objects.get(id=request.session['patient_id'])
    patient.physician_code = ''.join(random.choices(string.ascii_letters + string.digits, k=code_length))
    patient.physician_code_created = datetime.now()

    return render(request, 'health_story/secondary/generate-physician-key.html',
                  {'patient': patient})




