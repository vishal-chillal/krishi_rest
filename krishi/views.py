from django.http import HttpResponse
from django.shortcuts import render
from function_api import FunctionAPI

fp = FunctionAPI()


def index(request):
    return HttpResponse("Hello, world. You're at the krishi index.")


def home(request):
    ''' handle post request from admin home'''
    username = "not loged in"
    resp = {}
    if request.method == "POST":
        data = fp.clean_json(request.body)
        if fp.validate_login(data):
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


def showEventDetails(req, myEvnt):
    res = fp.getEvent(myEvnt)
    html = "<table>"
    for i in res.items():
        html += "<tr><td>" + str(i[0])
        html += "</td><td>" + str(i[1])
        html += "</td></tr>"
    html += "</table>"
    return HttpResponse(html)


def userhome(request):
    ''' handle request from enduser home'''
    resp = {}
    if request.method == "POST":
        data = fp.clean_json(request.body)
        if fp.validate_userlogin(data):
            username = data['username']
            html = '<h1>All Events</h1><br><div>'
            allevents = fp.getAllEvents()
            request.session['username'] = username

            for each in allevents.items():
                html += "<a href="
                url_name = str(each[0])
                html += url_name + ">"
                html += str(each[1]) + "</a><br>"
            html += '</div><br><br><h1>My Events</h1><br><div>'

            myevents = fp.getMyEvents(username)
            for each in myevents:
                html += "<a href=" + str(each[0]) \
                    + ">" + str(each[1]) + "</a><br>"
            html = html + '</div><br><div>'
            return HttpResponse(html)
        else:
            username = "not 123"
            resp["username"] = username
            return render(request, 'loggedin.html', resp)


def event(request):
    ''' admin panal handle event request '''
    if request.method == "GET":
        if 'username' in request.session:
            return HttpResponse(request.session['username'])
        else:
            return HttpResponse("INVALID")

    elif request.method == "POST":
        data = fp.clean_json(request.body)
        return HttpResponse(fp.addEvent(data))


def signin(request):
    ''' admin signin request '''
    return render(request, 'login.html')


def usersignin(request):
    ''' end user signin request '''
    return render(request, 'userlogin.html')
