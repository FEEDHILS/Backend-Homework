from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import requests
from django.core.serializers import deserialize

GATEWAY_URL = "http://127.0.0.1:8001/get_data"

def index(req):
    if req.method == "POST":
        return gateway(req)

    return render(req, "index.html")

# Gateway к первому серверу, который выступает в роли db
def gateway(req):
    if req.method == "POST":
        try:
            response = requests.post(GATEWAY_URL, data=req.POST)
            return JsonResponse(response.json(), safe=False)
        
        except requests.RequestException as e:
            return HttpResponse(f"Error occurred: {e}", status=500)
    else:
        return redirect(index)