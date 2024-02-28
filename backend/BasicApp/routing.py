from django.urls import path

from BasicApp import consumers

ws_urlpatterns = [
    path('ws/page_tracking/', consumers.PageVisitConsumer.as_asgi()),
]
