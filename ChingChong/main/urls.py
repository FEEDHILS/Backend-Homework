from django.urls import path, include
from . import views
from .models import User

urlpatterns = [
    path('', views.index, name="index"),
    path('', include('django.contrib.auth.urls')),
    path('registration/', views.reg, name="registration"),
    path('delete/', views.delete, name="delete"),
    path('reset/', views.reset, name="reset"),
    path('change/<uidb64>/<token>/', views.change_password, name="change_password_validation")
]