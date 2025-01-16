from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from .forms import *


def index(req):
    EditForm = None
    if req.user.is_authenticated:
        if req.method == "GET":
            data = { "username": req.user.username, "email": req.user.email }
            EditForm = UserEditForm(initial=data, instance=req.user)

        else:
            EditForm = UserEditForm(data=req.POST, instance=req.user)
            if EditForm.is_valid():
                req.user.username = req.POST["username"]
                req.user.email = req.POST["email"]
                req.user.save()
            else:
                # ModelForm меняет instance даже если валидация не проходит
                # Чтобы не выводился некорректный username, висит штука снизу
                req.user = User.objects.get(pk=req.user.pk)
    
    return render(req, "index.html", { "form": EditForm }) 
        
def reg(req):
    if req.method == "GET":
        RegisterForm = UserRegisterForm()
    
    else:
        RegisterForm = UserRegisterForm(req.POST)
        if RegisterForm.is_valid():
            NewUser = RegisterForm.save()
            login(req, NewUser)
            return redirect(index)

    return render(req, "registration.html", { "form": RegisterForm })

def reset(req):
    if req.method == "GET":
        EmailForm = PasswordResetForm()
    else:
        EmailForm = PasswordResetForm(req.POST)
        if EmailForm.is_valid():
            EmailForm.save(request=req)

    return render(req, "reset.html", { "form": EmailForm }) 

def change_password(req, uidb64, token):
    id = urlsafe_base64_decode(uidb64).decode()
    user = User.objects.get(pk=id)

    if PasswordResetTokenGenerator().check_token(user, token):
        if req.method == "GET":
            PassForm = SetPasswordForm(user=user)
        else:
            PassForm = SetPasswordForm(user, req.POST)
            if PassForm.is_valid():
                PassForm.save()
                print("Password has Changed")
                return redirect(index)

        return render(req, "change.html", { "form": PassForm }) 
    else:
        return redirect(index)

def delete(req):
    if req.user.is_authenticated:
        req.user.delete()
        return redirect(index)
