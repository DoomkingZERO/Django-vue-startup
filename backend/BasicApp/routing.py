from django.urls import path

from .consumers import TrackConsumer

ws_urlpatterns = [
    path('ws/track/', TrackConsumer.as_asgi())
]