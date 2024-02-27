from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import JsonResponse


def get_users(request):
    users = User.objects.all().values('id', 'username', 'email')
    return JsonResponse({'users': list(users)})


def home_view(request):

    return render(request, 'BasicApp/home.html')
