from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import User

# Главная страница (Вход в пользователя).
def index(req):
    if req.method == "GET":
        return render(req, "index.html", {})

# Эндпоинт проверки данных.
def auth(req):
    if req.method == "POST":
        # Проверяем есть ли пользователь с такими данными в БД.
        login = req.POST['login']
        password = req.POST['pass']
        
        try:
            user = User.objects.get(login=login, password=password)
        except User.DoesNotExist:
            return HttpResponse("Такого пользователя не существует, зарегестрируйтесь.")

        return redirect(greet, user.pk)

# Страница с регистрацией.
def reg(req):
    if req.method == "GET":
        return render(req, "register.html", {})
    
    if req.method == "POST":
        # Создаем пользователя
        new_user = User()
        new_user.login = req.POST['login']
        new_user.name = req.POST['name']
        new_user.password = req.POST['pass']
        
        # Ищем дубликат по логину
        try:
            User.objects.get(login=new_user.login)
        except User.DoesNotExist:
            new_user.save()
            return redirect(greet, new_user.pk)
        
        return render(req, "register.html", {"error": "Такой логин уже используется."})


def greet(req, id):
    # Ищем пользователя, и если не находим, выводим ошибку.
    try:
        name = User.objects.get(id=id).name
        return HttpResponse("Дарова " + name)
    except User.DoesNotExist:
        return HttpResponse("Ошибка, такого пользователя не существует") 