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

def showEventDetailsAdmin(req, myEvnt):
    res = fp.getEvent(myEvnt)
    html = getEventDetailsTable(myEvnt)
    return HttpResponse(html)

def showEventDetails(req, myEvnt):
    res = fp.getEvent(myEvnt)
    html = getEventDetailsTable(myEvnt)
    if res[u'id'] not in fp.myEventList.keys() and fp.getEventCapacity(myEvnt) == 0 :
            html += "<br><br><h6>SEATS UNAVAILABLE</h6>"
    else:
        if res[u'id'] not in fp.myEventList.keys():
            subscribe = "SUBSCRIBE_"
        elif res[u'id'] in fp.myEventList.keys():
            subscribe = "UNSUBSCRIBE_"
        html += "<a href=" + subscribe + str(res[u'id']) + ">"
        html += subscribe[:-1] + "</a>"
    return HttpResponse(html)


def getEventDetailsTable(myEvnt):
    res = fp.getEvent(myEvnt)
    html = "<table>"
    for i in res.items():
        html += "<tr><td>" + str(i[0])
        html += "</td><td>" + str(i[1])
        html += "</td></tr>"
    html += "</table>"
    return html


def handle_event(request, evnt):
    username = request.session["username"]
    # return HttpResponse(str(request.body) + "  asd")
    if("UNSUBSCRIBE" not in evnt):
        return HttpResponse(fp.subscribe(evnt, username))
    else:
        return HttpResponse(fp.unsubscribe(evnt, username))


def userhome(request):
    ''' handle request from enduser home'''
    resp = {}
    if request.method == "POST":
        data = fp.clean_json(request.body)
        if fp.validate_userlogin(data):
            username = data['username']
            request.session["username"] = username
            html = fp.generateAllEventList()
            html += '<br><h1>My Events</h1><br><div>'

            myevents = fp.getMyEvents(username)
            for each in myevents.items():
                html += "<a href=" + str(each[0]) \
                    + ">" + str(each[1]) + "</a><br>"
            html = html + '</div><br><div>'
            html += username
            return HttpResponse(html)
        else:
            username = "not 123"
            resp["username"] = username
            return render(request, 'loggedin.html', resp)


def event(request):
    ''' admin panal handle event request '''
    if request.method == "GET":
        if 'username' in request.session:
            html = fp.generateAllEventList()
            return HttpResponse(html)
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
