from django.shortcuts import render


def home(request):
    user = request.user
    return render(request, 'health_story/home.html', {'user': user})
