import json
from krishi.models import UserInfo


user_details = UserInfo.objects.values()


def clean_json(request):
    ls = request.split('&')
    dic = {}
    for x in ls:
        dic[x.split('=')[0]] = x.split('=')[1]
    return json.dumps(dic)


def validate_login(req):
    response = False
    for entry in user_details:
        if(entry["user"] == req["username"] and entry["password"] == req["password"]):
            response = True
            break
    return response
