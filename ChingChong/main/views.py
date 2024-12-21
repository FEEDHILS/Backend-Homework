from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from .models import User


def index(req):
    context = {'Users': User.objects.all()}
    return render(req, "index.html", context)


def create(req):
    if req.method == "GET":
        return render(req, "register.html")
    if req.method == "POST":
        new_user = User()
        new_user.login = req.POST['login']
        new_user.name = req.POST['name']
        new_user.password = req.POST['pass']
        new_user.save()
        
        return redirect(index)
            

def read(req, id):
    if req.method == "GET":
        return render(req, "read.html", {'User':User.objects.get(pk=id)})

def update(req, id):
    if req.method == "POST":
        user = User.objects.get(pk=id)
        user.login = req.POST['login']
        user.name = req.POST['name']
        user.password = req.POST['pass']
        user.save()
        
        return redirect( read, id )

def delete(req, id):
    User.objects.get(pk=id).delete()
    return redirect(index)