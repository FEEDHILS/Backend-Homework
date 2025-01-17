from django.urls import path, include
from . import views
from .models import User

urlpatterns = [
    path('get_data', views.get_data),
]