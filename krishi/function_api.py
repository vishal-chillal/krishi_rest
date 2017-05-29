from krishi.models import UserInfo, Event, EndUser, Subscription

user_details = UserInfo.objects.values()
enduser_details = EndUser.objects.values()
event_details = {}
allEventList = {}


def clean_json(request):
    ''' get the request body and convert it into clean json '''
    ls = request.split('&')
    dic = {}
    for x in ls:
        dic[x.split('=')[0]] = x.split('=')[1]
    # return json.dumps(dic)
    return dic


def validate_login(req):
    ''' validate username and password of admin user '''
    response = False
    for entry in user_details:
        if entry["user"] == req["username"] and\
                entry["password"] == req["password"]:

            response = True
            break
    return response


def validate_userlogin(req):
    ''' validate username and password of enduser '''
    response = False
    for entry in enduser_details:
        if entry["username"] == req["username"] and\
                entry["password"] == req["password"]:

            response = True
            break
    return response


def getAllEvents():
    ''' get  all events avalable to subscribe '''
    event_details = Event.objects.values()
    for eachevent in event_details:
        allEventList[eachevent["id"]] = eachevent["eventname"]
    return allEventList


def getMyEvents(username):
    myEventList = []
    query = "SELECT * from krishi_subscription\
                where username = '" + username + "'"

    event_lst = Subscription.objects.raw(query)
    for eachevent in event_lst:
        myEventList.append(allEventList[eachevent.eventid])

    return myEventList


def getEvent(id):
    res = "new"
    for eachevent in event_details:
        if eachevent["id"] == id:
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
