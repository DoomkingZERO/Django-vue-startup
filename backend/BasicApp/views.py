import json

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import PageVisit
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)


def get_users(request):
    users = User.objects.all().values('id', 'username', 'email')
    return JsonResponse({'users': list(users)})


@csrf_exempt
def create_page_visit(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(f'data {data}')
        page_id = data.get('page_id')
        user_id = data.get('user_id')

        page_visit = PageVisit.objects.filter(page_id=page_id, user_id=user_id).first()

        if page_visit:
            # If the object exists, update the stop_time
            # Also update the stop_time
            # Also add in a ping count
            page_visit.start_time = timezone.now()
            page_visit.save()
        else:
            # If the object doesn't exist, create it
            PageVisit.objects.create(
                user_id=user_id,
                page_id=page_id,
                start_time=timezone.now(),
                stop_time=timezone.now() + timedelta(seconds=30)
            )
        page_visit_count = PageVisit.objects.filter(page_id=page_id, start_time__gte=timezone.now() - timedelta(seconds=30)).count()

        # Return a JsonResponse to indicate success
        return JsonResponse({'message': f'Viewed by number {page_visit_count}'})

    # Handle other HTTP methods if necessary
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)
