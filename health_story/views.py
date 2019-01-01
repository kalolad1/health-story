from django.shortcuts import render
from .models import Patient


def home(request):
    patient = Patient.objects.get(username=request.user.username)
    return render(request, 'health_story/home.html', {'patient': patient})
