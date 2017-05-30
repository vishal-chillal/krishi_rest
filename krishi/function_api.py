from krishi.models import UserInfo, Event, EndUser, Subscription


class FunctionAPI(object):
    """docstring for FunctionAPI"""
    def __init__(self):
        self.user_details = UserInfo.objects.values()
        self.enduser_details = EndUser.objects.values()
        self.event_details = {}
        self.allEventList = {}
        self.myEventList = {}
        self.counter = 0
        self.Subscription_count = 0

    def clean_json(self, request):
        ''' get the request body and convert it into clean json '''
        ls = request.split('&')
        dic = {}
        for x in ls:
            dic[x.split('=')[0]] = x.split('=')[1]
        return dic

    def validate_login(self, req):
        ''' validate username and password of admor9in user '''
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


    def generateAllEventList(self):
        html = '<h1>All Events</h1><br><div>'
        allevents = self.getAllEvents()
        for each in allevents.items():
            html += "<a href="
            url_name = str(each[0])
            html += url_name + ">"
            html += str(each[1]) + "</a><br>"
        html += '</div><br>'
        return html


    def getAllEvents(self):
        ''' get  all events avalable to subscribe '''
        self.counter += 1
        self.event_details = Event.objects.values()
        for eachevent in self.event_details:
            self.allEventList[eachevent["id"]] = eachevent["eventname"]
        return self.allEventList

    def getMyEvents(self, username):
        query = "SELECT * from krishi_subscription where username = '" + username + "'"

        event_lst = Subscription.objects.raw(query)
        for eachEvnt in event_lst:
            value = self.allEventList[eachEvnt.eventid]
            self.myEventList[eachEvnt.eventid] = value

        return self.myEventList

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

    def getEventCapacity(self,eventid):
        return Event.objects.filter(id=eventid).values()[0]["capacity"]


    def updateEventCapacity(self, decision, eventid):
        try:
            currentCapacity = self.getEventCapacity(eventid)
            currentCapacity += decision
            Event.objects.filter(id=1).update(capacity = currentCapacity)
            return True
        except Exception as e:
            print e
            return False        

    def unsubscribe(self, event, username):
        id = int(event.split('_')[1])
        try:
            Subscription.objects.filter(username=username).delete()
            del(self.myEventList[id])
            return self.updateEventCapacity(1,id)
        except Exception as e:
            return str(e)

    def subscribe(self, event, username):
        s = Subscription()
        s.eventid = int(event.split('_')[1])
        s.username = username
        id = self.Subscription_count
        s.id = id
        try:
            s.save()
            self.Subscription_count += 1
            return self.updateEventCapacity(-1,s.eventid)
        except Exception, e:
            return s.eventid, e
