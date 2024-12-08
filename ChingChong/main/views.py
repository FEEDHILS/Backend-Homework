from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(req):
    if req.method == "GET":
        return render(req, "index.html", {})
    
def auth(req):
    if req.method == "GET":
        return render(req, "auth.html", {})
    
def result(req):
    if req.method == "POST":
        data = {'name' : req.POST['fname'] + " " + req.POST['lname']}
        return render(req, "result.html", data)
