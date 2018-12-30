from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User


def login(request):
    """Handles login page functionality.

    Responsible for two separate things: to show the login page, and to handle a
    request to login.

    Args:
        request: A HttpRequest object.

    Returns:
        A redirect to the health story home page, login screen for the first time, or back to
        the login screen if user entered invalid credentials.
    """
    # User submits login credentials.
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # User was able to be logged in successful. Sends them to the health story home page.
            auth.login(request, user)
            return redirect('health_story/home')
        else:
            # Either the username or password was incorrect. Sends them back to the login page.
            return render(request, 'accounts/login.html', {'error': 'Username or password is incorrect.'})

    # Displays login page.
    return render(request, 'accounts/login.html')


def sign_up(request):
    """Handles sign up page functionality.

    Responsible for two separate things: to show the sign up page or to handle a
    request to sign up.

    Args:
        request: A HttpRequest object.

    Returns:
        A redirect to the health story home page, sign up screen for the first time, or back to
        the sign up screen if user entered an existing username.
    """
    # User submits sign up credentials.
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        password_check = request.POST['pass-check']

        if password == password_check:
            try:
                # A user with inputted username already exists. Send the user an error.
                User.objects.get(username=username)
                return render(request, 'accounts/sign-up.html', {'error': 'Username already exists!'})
            except User.DoesNotExist:
                # No existing user exists, create user successfully and bring them to the home page.
                user = User.objects.create_user(username=username, password=password)
                auth.login(request, user)
                return redirect('health_story/home')
        else:
            # User failed to enter two passwords that matched.
            return render(request, 'accounts/sign-up.html', {'error': 'Passwords do not match!'})

    # Displays sign up page.
    return render(request, 'accounts/sign-up.html')


def logout(request):
    """Handles a logout request.

    Responsible for logging the user out and bringing them to the landing page.

    Args:
        request: A HttpRequest object.

    Returns:
        A redirect to the landing page.
    """
    if request.method == 'POST':
        auth.logout(request)
        return redirect('landing-page')

