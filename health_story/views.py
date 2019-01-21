from django.shortcuts import render, redirect
from .models import Patient, HealthEncounter, Relative
from django.contrib.auth.decorators import login_required
from django.core import serializers
from datetime import datetime, date
from .helper.constants import MPConstants, PAConstants
from .helper import choices
import random
import string


@login_required
def set_up(request, should_redirect=True):
    """Caches important patient information using cookies.

    This function is called each time user enters a new session.
    It is used to store cookies to prevent unnecessary database queries.
    """
    patient = Patient.objects.get(username=request.user.username)
    info = patient.get_all_patient_info()

    request.session[PAConstants.PATIENT_ID] = patient.id
    request.session[MPConstants.MEDICATIONS] = serializers.serialize('json', info[MPConstants.MEDICATIONS])
    request.session[MPConstants.CONDITIONS] = serializers.serialize('json', info[MPConstants.CONDITIONS])

    if should_redirect:
        return redirect('health_story/demographics')


# Main pages.
@login_required
def demographics(request):
    patient = Patient.objects.get(id=request.session[PAConstants.PATIENT_ID])
    ui_info = patient.get_info_for_ui(MPConstants.DEMOGRAPHICS)
    return render(request, 'health_story/demographics.html', {'patient': patient,
                                                              'ui_info': ui_info})


@login_required
def vitals(request):
    patient = Patient.objects.get(id=request.session[PAConstants.PATIENT_ID])
    ui_info = patient.get_info_for_ui(MPConstants.VITALS)
    return render(request, 'health_story/vitals.html', {'patient': patient,
                                                        'ui_info': ui_info})


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
def display_medications(request):
    patient = Patient.objects.get(id=request.session[PAConstants.PATIENT_ID])

    deserialized_objects = serializers.deserialize('json', request.session[MPConstants.MEDICATIONS])
    medications = [medications.object for medications in deserialized_objects]

    return render(request, 'health_story/medications.html',
                  {'patient': patient, MPConstants.MEDICATIONS: medications})


@login_required
def display_conditions(request):
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
    patient.save()

    return render(request, 'health_story/secondary/generate-physician-key.html',
                  {'patient': patient})


@login_required
def edit_patient_info(request):
    patient = Patient.objects.get(id=request.session[PAConstants.PATIENT_ID])

    if request.method == 'POST':
        # Demographic info
        if request.POST['origin'] == MPConstants.DEMOGRAPHICS:
            # TODO put placeholder to indicate correct format
            patient.date_of_birth = datetime.strptime(request.POST['Date of Birth'], '%b %d %Y').date()
            patient.email = request.POST['Email']
            patient.race = request.POST['Race']
            patient.sex = request.POST['Sex']
            patient.save()
            return redirect('health_story/demographics')


# Add or modify pages.
@login_required
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
            conditions = request.POST['conditions'].split(', ')
            medications = request.POST['medications'].split(', ')

            health_encounter = HealthEncounter()
            health_encounter.patient = patient
            health_encounter.physician = "{fn} {ln}".format(fn=first_name, ln=last_name)
            health_encounter.location = location
            health_encounter.type_of_encounter = type_of_encounter
            health_encounter.description = description
            health_encounter.save()

            for condition in conditions:
                health_encounter.conditions.create(name=condition)

            for medication in medications:
                health_encounter.medications.create(name=medication)

            health_encounter.save()
            set_up(request, False)
            return redirect('health_story/timeline')
        except KeyError:
            error = 'Please enter complete fields before adding!'
            return render(request, 'health_story/modify_views/add-health-encounter.html', {'patient': patient,
                                                                                           'type_options': type_options,
                                                                                           'error': error})

    return render(request, 'health_story/modify_views/add-health-encounter.html', {'patient': patient,
                                                                                   'type_options': type_options})


@login_required
def add_family_history(request):
    patient = Patient.objects.get(id=request.session['patient_id'])
    type_options = [i[1] for i in choices.TYPE_OF_RELATIONSHIP]
    if request.method == 'POST':
        try:
            full_name = request.POST['full-name']
            type_of_relationship = request.POST['type-of-relationship']
            conditions = request.POST['conditions'].split(', ')

            relative = Relative()
            relative.full_name = full_name
            relative.type_of_relationship = type_of_relationship
            relative.save()

            for condition in conditions:
                relative.conditions.create(name=condition)

            relative.save()
            patient.relatives.add(relative)
            return redirect('health_story/family_history')
        except KeyError:
            error = "Please enter all fields!"
            return render(request, 'health_story/modify_views/add-family-history.html', {'patient': patient,
                                                                                         'type_options': type_options,
                                                                                         'error': error})

    return render(request, 'health_story/modify_views/add-family-history.html', {'patient': patient,
                                                                                 'type_options': type_options})






