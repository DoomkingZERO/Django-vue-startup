from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import PageVisit
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


def get_users(request):
    users = User.objects.all().values('id', 'username', 'email')
    return JsonResponse({'users': list(users)})


@csrf_exempt
def create_page_visit(request):
    if request.method == 'POST':
        page_id = request.POST.get('page_id')
        user_id = request.POST.get('user_id')

        page_visit = PageVisit.objects.filter(page_id=page_id, user_id=user_id).first()

        if page_visit:
            # If the object exists, update the stop_time
            page_visit.stop_time = timezone.now()
            page_visit.save()
        else:
            # If the object doesn't exist, create it
            PageVisit.objects.create(
                user_id=user_id,
                page_id=page_id,
                start_time=timezone.now(),
                stop_time=timezone.now()
            )

        # Return a JsonResponse to indicate success
        return JsonResponse({'message': 'Page visit recorded successfully'})

    # Handle other HTTP methods if necessary
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)
