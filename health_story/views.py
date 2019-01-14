from django.shortcuts import render, redirect
from .models import Patient, HealthEncounter
from django.contrib.auth.decorators import login_required
from .helper import choices, constants


# Main pages.
@login_required
def home(request):
    patient = Patient.objects.get(username=request.user.username)

    # Sets the patient_id to be used on every other page.
    # TODO store actually patient object, if possible, not id, to avoid
    # TODO redundant queries.
    request.session['patient_id'] = patient.id
    return render(request, 'health_story/home.html', {'patient': patient})


@login_required
def demographics(request):
    patient = Patient.objects.get(id=request.session['patient_id'])
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


# Add or modify pages.
def add_health_encounter(request):
    patient = Patient.objects.get(id=request.session['patient_id'])
    type_options = [i[1] for i in choices.TYPE_OF_HEALTH_ENCOUNTER]

    if request.method == 'POST':
        try:
            first_name = request.POST['first-name']
            last_name = request.POST['last-name']
            location = request.POST['location']
            type_of_encounter = request.POST['type-of-encounter'].lower()
            description = request.POST['description']

            health_encounter = HealthEncounter()
            health_encounter.patient = patient
            health_encounter.physician = "{fn} {ln}".format(fn=first_name, ln=last_name)
            health_encounter.location = location
            health_encounter.type_of_encounter = type_of_encounter
            health_encounter.description = description
            health_encounter.save()
            return redirect('health_story/timeline')
        except KeyError:
            error = 'Please enter complete fields before adding!'
            return render(request, 'health_story/modify_views/add-health-encounter.html', {'patient': patient,
                                                                                           'type_options': type_options,
                                                                                           'error': error})
    else:
        return render(request, 'health_story/modify_views/add-health-encounter.html', {'patient': patient,
                                                                                       'type_options': type_options})
