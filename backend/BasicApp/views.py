from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import SimplePageVisit


def get_users(request):
    users = User.objects.all().values('id', 'username', 'email')
    return JsonResponse({'users': list(users)})


def home_view(request):

    return render(request, 'BasicApp/home.html')


def create_page_visit_object(page_id, user_id):
    page_id = 'page_id'
    user_id = 'user_id'

    try:
        simple_page_visit = SimplePageVisit.objects.create(
            user_id=user_id,
            page_id=page_id,
        )
        return JsonResponse({'success': True, 'message': 'Object created successfully.', 'simple_page_visit': {simple_page_visit}})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})

