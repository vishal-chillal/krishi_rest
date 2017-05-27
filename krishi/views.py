from django.http import HttpResponse
from django.shortcuts import render
from function_api import *
import json


def index(request):
    return HttpResponse("Hello, world. You're at the krishi index.")


def login(request):
    username = "not loged in"
    resp = {}
    if request.method == "POST":
        data = clean_json(request.body)
        data = json.loads(data)
        if validate_login(data):
            username = data['username']
            resp["status"] = 201
            resp["message"] = "logged in"
            resp["username"] = username
    else:
        username = "not 123"
        resp["status"] = 403
        resp["message"] = "Invalid"
        resp["username"] = username
    return render(request, 'loggedin.html', resp)


def signin(request):
    return render(request, 'login.html')
