from .models import AuthKey
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render, redirect
from health_story.models import Patient
from measurement.measures import Weight, Distance


def login_page(request):
    """Displays the login page."""
    return render(request, 'accounts/login.html')


def login_patient(request):
    """Handles login page functionality for a patient.

    Responsible for two separate things: to show the login page, and to handle a
    request to login.

    Args:
        request: A HttpRequest object.

    Returns:
        A redirect to the health story home page, login screen for the first
        time, or back to the login screen if user entered invalid credentials.
    """
    # User submits login credentials.
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # User was able to be logged in successful.
            auth.login(request, user)

            # Check if they filled out the registration form.
            if not Patient.is_user_registered(user.username):
                return redirect('accounts/patient-registration')

            return redirect('health_story/set_up')
        else:
            # Either the username or password was incorrect. Sends them back to
            # the login page.
            return render(request, 'accounts/login.html',
                          {'error': 'Username or password is incorrect.'})


def login_physician(request):
    """Handles login page functionality for a physician.

    Responsible for two separate things: to show the login page, and to handle a
    request to login.

    Args:
        request: A HttpRequest object.

    Returns:
        A redirect to the health story home page, login screen for the first
        time, or back to the login screen if user entered invalid credentials.
    """
    # User submits login credentials.
    if request.method == 'POST':
        # TODO add a username too
        physician_key = request.POST['physician-key']
        auth_key = request.POST['authentication-key']

        try:
            AuthKey.objects.get(key=auth_key)

            patient = None
            for pat in Patient.objects.all():
                if pat.is_physician_code_valid(physician_key):
                    patient = pat

            if not patient:
                raise KeyError
        except KeyError:
            error = "You entered an incorrect key."
            return render(request, 'accounts/login.html', {'error': error})

        patient.admin_mode = True
        patient.save()
        user = User.objects.get(username=patient.username)
        auth.login(request, user)
        return redirect('health_story/set_up')


def sign_up(request):
    """Handles sign up page functionality.

    Responsible for two separate things: to show the sign up page or to handle a
    request to sign up.

    Args:
        request: A HttpRequest object.

    Returns:
        A redirect to the health story home page, sign up screen for the first
        time, or back to the sign up screen if user entered an existing username.
    """
    # User submits sign up credentials.
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        password_check = request.POST['pass-check']

        if password == password_check:
            try:
                # A user with inputted username already exists
                User.objects.get(username=username)
                return render(request, 'accounts/sign-up.html',
                              {'error': 'Username already exists!'})
            except User.DoesNotExist:
                # No existing user exists, create user successfully and bring
                # them to the home page.
                user = User.objects.create_user(username=username,
                                                password=password)
                auth.login(request, user)
                return redirect('accounts/patient-registration')
        else:
            # User failed to enter two passwords that matched.
            return render(request, 'accounts/sign-up.html',
                          {'error': 'Passwords do not match!'})

    # Displays sign up page.
    return render(request, 'accounts/sign-up.html')


def patient_registration(request):
    if request.method == 'POST':
        # Obtain information and create patient model
        try:
            first_name = request.POST['first-name']
            last_name = request.POST['last-name']
            date_of_birth = request.POST['date-of-birth']
            email = request.POST['email']
            sex = request.POST['sex']
            race = request.POST['race']
            weight = request.POST['weight']
            height = request.POST['height']

        # User did not fill out all fields.
        except KeyError:
            error = "Please fill out all the fields!"
            return render(request, 'accounts/patient-registration.html',
                          {'error': error})

        patient = Patient()
        patient.username = request.user
        patient.first_name = first_name
        patient.last_name = last_name
        patient.date_of_birth = date_of_birth
        patient.email = email
        patient.sex = sex
        patient.race = race
        patient.weight = Weight(lb=weight)
        patient.height = Distance(inches=height)
        patient.save()

        return redirect('health_story/set_up')
    else:
        return render(request, 'accounts/patient-registration.html')


def logout(request):
    """Handles a logout request.

    Responsible for logging the user out and bringing them to the landing page.
    It also sets the admin_mode to false.

    Args:
        request: A HttpRequest object.

    Returns:
        A redirect to the landing page.
    """
    patient = Patient.objects.get(username=request.user.username)
    patient.admin_mode = False
    patient.save()
    auth.logout(request)
    return redirect('landing-page')
