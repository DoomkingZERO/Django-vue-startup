from django.urls import path
from . import views

app_name = "BasicApp"

urlpatterns = [
    path('api/users/', views.get_users, name='get_users'),
    path('api/create_page_visit/', views.create_page_visit_object, name='create_page_visit_object'),
    path('home', views.home_view, name="home")
]
