from django.shortcuts import render
from .models import Patient


def home(request):
    patient = Patient.objects.get(username=request.user.username)

    # Sets the patient_id to be used on every other page.
    # TODO store actually patient object, if possible, not id, to avoid
    # TODO redundant queries.
    request.session['patient_id'] = patient.id
    return render(request, 'health_story/home.html', {'patient': patient})


def timeline(request):
    patient = Patient.objects.get(id=request.session['patient_id'])
    return render(request, 'health_story/timeline.html', {'patient': patient})


def demographics(request):
    patient = Patient.objects.get(id=request.session['patient_id'])
    return render(request, 'health_story/demographics.html', {'patient': patient})


def vitals(request):
    patient = Patient.objects.get(id=request.session['patient_id'])
    return render(request, 'health_story/vitals.html', {'patient': patient})

