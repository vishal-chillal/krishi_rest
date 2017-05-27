import json
from krishi.models import UserInfo, Event, EndUser


user_details = UserInfo.objects.values()
enduser_details = EndUser.objects.values()
event_details = Event.objects.values()


def clean_json(request):
    ls = request.split('&')
    dic = {}
    for x in ls:
        dic[x.split('=')[0]] = x.split('=')[1]
    #return json.dumps(dic)
    return dic

def validate_login(req):
    response = False
    for entry in user_details:
        if(entry["user"] == req["username"] and entry["password"] == req["password"]):
            response = True
            break
    return response

def validate_userlogin(req):
    response = False
    for entry in enduser_details:
        if(entry["username"] == req["username"] and entry["password"] == req["password"]):
            response = True
            break
    return response

def getAllEvents():
    event_details = Event.objects.values()
    return event_details

# def getMyEvents(username):
#     myEventList = []
#     for eachevent in Event.objects.raw("SELECT * from krishi_event where user")
#     return 

def getEvent(req,id):
    res = ""
    for eachevent in event_details:
        if eachevent["id"] == req["id"]:
            res = eachevent
            break
    return res

def addEvent(req):
    obj = Event()
    obj.capacity = req["capacity"]
    obj.description = req["description"]
    obj.eventname = req["eventname"]
    obj.location = req["location"]
    obj.fees = req["fees"]
    obj.startdate = req["startdate"]
    obj.enddate = req["enddate"]
    obj.info = req["info"]
    try:
        obj.save()
        return True
    except Exception as e:
        print e
        return False