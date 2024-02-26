from django.urls import path
from . import views
from .consumers import PageVisitConsumer

app_name = "BasicApp"

urlpatterns = [
    path('api/users/', views.get_users, name='get_users'),
]

websocket_urlpatterns = [
    path('ws/page_tracking/', PageVisitConsumer.as_asgi(), name='page_tracking_ws'),
]
