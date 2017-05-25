from django.http import HttpResponse
from django.shortcuts import render
from function_api import *
import json


def index(request):
    return HttpResponse("Hello, world. You're at the krishi index.")


def login(request):
    username = "not loged in"
    if request.method == "POST":
        data = clean_json(request.body)
        data = json.loads(data)
        if validate_login(data):
            username = data['username']
    return render(request, 'loggedin.html', {"username": username})


def signin(request):
    return render(request, 'login.html')
