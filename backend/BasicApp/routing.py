from django.conf.urls import url

from backend.BasicApp import consumers

ws_urlpatterns = [
    url('ws/page_tracking/', consumers.PageVisitConsumer),
]
