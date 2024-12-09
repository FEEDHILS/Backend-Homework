from django.urls import path
from . import views
from .models import User

urlpatterns = [
    path('', views.index),
    path('reg', views.reg),
    path('auth', views.auth),
    # Чтобы можно было передавать пользователей (их id)
    path('greet/id/<int:id>', views.greet),
]
