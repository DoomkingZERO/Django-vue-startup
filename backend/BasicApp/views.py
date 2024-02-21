from django.contrib.auth.models import User
from django.http import JsonResponse


def get_users(request):
    users = User.objects.all().values('id', 'username', 'email')
    return JsonResponse({'users': list(users)})
