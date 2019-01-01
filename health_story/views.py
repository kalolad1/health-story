from django.shortcuts import render
from .models import Patient


def home(request):
    patient = Patient.objects.get(username=request.user.username)

    # Sets the patient_id to be used on every other page.
    request.session['patient_id'] = patient.id
    return render(request, 'health_story/home.html', {'patient': patient})


def timeline(request):
    patient = Patient.objects.get(id=request.session['patient_id'])
    return render(request, 'health_story/timeline.html', {'patient': patient})
