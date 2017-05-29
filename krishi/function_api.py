from krishi.models import UserInfo, Event, EndUser, Subscription


class FunctionAPI(object):
    """docstring for FunctionAPI"""
    def __init__(self):
        self.user_details = UserInfo.objects.values()
        self.enduser_details = EndUser.objects.values()
        self.event_details = {}
        self.allEventList = {}
        self.counter = 0

    def clean_json(self, request):
        ''' get the request body and convert it into clean json '''
        ls = request.split('&')
        dic = {}
        for x in ls:
            dic[x.split('=')[0]] = x.split('=')[1]
        # return json.dumps(dic)
        return dic

    def validate_login(self, req):
        ''' validate username and password of admin user '''
        response = False
        for entry in self.user_details:
            if entry["user"] == req["username"] and\
                    entry["password"] == req["password"]:

                response = True
                break
        return response

    def validate_userlogin(self, req):
        ''' validate username and password of enduser '''
        response = False
        for entry in self.enduser_details:
            if entry["username"] == req["username"] and\
                    entry["password"] == req["password"]:

                response = True
                break
        return response

    def getAllEvents(self):
        ''' get  all events avalable to subscribe '''
        self.counter += 1
        self.event_details = Event.objects.values()
        for eachevent in self.event_details:
            self.allEventList[eachevent["id"]] = eachevent["eventname"]
        return self.allEventList

    def getMyEvents(self, username):
        myEventList = []
        query = "SELECT * from krishi_subscription\
                    where username = '" + username + "'"

        event_lst = Subscription.objects.raw(query)
        for eachevent in event_lst:
            myEventList.append((eachevent.eventid, self.allEventList[eachevent.eventid]))

        return myEventList

    def getEvent(self, id):
        res = {}
        for eachevent in self.event_details:
            if str(eachevent["id"]) == str(id):
                res = eachevent
                break
        return res

    def addEvent(self, req):
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
