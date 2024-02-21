from django.urls import path
from . import views

app_name = "BasicApp"

urlpatterns = [
    path('api/users/', views.get_users, name='get_users'),
]
