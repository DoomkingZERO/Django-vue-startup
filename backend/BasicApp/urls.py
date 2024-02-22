from django.urls import path
from . import views

app_name = "BasicApp"

urlpatterns = [
    path('api/users/', views.get_users, name='get_users'),
    path('api/users/page', views.create_page_visit, name='create_page_visit'),
]
