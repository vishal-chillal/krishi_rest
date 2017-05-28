from django.http import HttpResponse
from django.shortcuts import render
from function_api import *
import json


def index(request):
    return HttpResponse("Hello, world. You're at the krishi index.")


def home(request):
    username = "not loged in"
    resp = {}
    if request.method == "POST":
        data = clean_json(request.body)
        #data = json.loads(data)
        if validate_login(data):
            username = data['username']
            resp["status"] = 201
            resp["message"] = "logged in"
            resp["username"] = username
            request.session['username'] = username
            return render(request, 'event.html', resp)
        else:
            username = "not 123"
            resp["status"] = 403
            resp["message"] = "Invalid"
            resp["username"] = username
            print request
            return render(request, 'loggedin.html', resp)

def userhome(request):
    #username = "not loged in"
    resp = {}
    if request.method == "POST":
        data = clean_json(request.body)
        #data = json.loads(data)
        if validate_userlogin(data):
            username = data['username']
            html = '<h1>All Events</h1><br><div>'
            allevents = getAllEvents()
            request.session['username'] = username
            #return HttpResponse(allevents) #

            for eachevent in allevents.items():
                html += "<a href="+str(eachevent[1])+">"+str(eachevent[1])+"</a><br>"
            html = html + '</div><br><br><h1>My Events</h1><br><div>'

            myevents = getMyEvents(username)
            for eachevent in myevents:
                html += "<a href="+str(eachevent)+">"+str(eachevent)+"</a><br>"
            html = html + '</div><br><div>'
            return HttpResponse(html) #
        else:
            username = "not 123"
            resp["username"] = username
            print request
            return render(request, 'loggedin.html', resp) #

def event(request):
    if request.method == "GET":
        if request.session.has_key('username'):
            print getAllEvents()
        #return HttpResponse()
            return HttpResponse(request.session['username'])
        else:
            return HttpResponse("INVALID")

    elif request.method == "POST":
        data = clean_json(request.body)
        return HttpResponse(addEvent(data))
        #return HttpResponse(request.data)

def signin(request):
    return render(request, 'login.html')

def usersignin(request):
    return render(request, 'userlogin.html')
