from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize

@csrf_exempt
def get_data(req):
    if req.method == "POST":
        data = serialize("json", User.objects.filter(username=req.POST["name"]))
        return JsonResponse(data, safe=False)
        