from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(req):
    if req.method == "GET":
        return render(req, "index.html",)
    if req.method == "POST":
        return redirect(auth, req.POST)
    
def auth(req):
    if req.method == "GET":
        return render(req, "auth.html",)
    if req.method == "POST":
        print(req.POST)
        return render(req, "auth.html", req.POST)

    
# def result(req):
#     if req.method == "POST":
#         data = {'name' : req.POST['fname'] + " " + req.POST['lname']}
#         return render(req, "result.html", data)
