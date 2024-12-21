from django.urls import path
from . import views
from .models import User

urlpatterns = [
    path('', views.index),
    path('read/<int:id>', views.read),
    path('create', views.create),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
    # # Чтобы можно было передавать пользователей (их id)
    # path('greet/id/<int:id>', views.greet),
    # path('test', views.testView.as_view()),
]