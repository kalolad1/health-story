from django.shortcuts import render, redirect
from health_story.models import Patient


def landing_page(request):
    """Displays the landing page, unless the user is logged in.

    If the user is logged in, redirect them to the homepage instead of
    the landing page.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse object.
    """
    if request.user.is_authenticated:
        if Patient.is_user_registered(username=request.user.username):
            return redirect('health_story/home')
        else:
            return redirect('accounts/patient-registration')

    return render(request, '../templates/landing-page.html')
