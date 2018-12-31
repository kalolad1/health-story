from django.shortcuts import render, redirect


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
        return redirect('health_story/home')

    return render(request, '../templates/landing-page.html')
