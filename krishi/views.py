from django.http import HttpResponseRedirect, HttpResponse
from krishi.forms import LoginForm
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the krishi index.")


def login(request):
    username = "not loged in"
    if request.method == "POST":
        MyLoginForm = LoginForm(request.POST)

        # username = MyLoginForm.cleaned_data['username']
        print request.body.split('&')[1]
        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
    else:
        MyLoginForm = LoginForm()
    return render(request, 'loggedin.html', {"username": username})
    # return render(request, 'login.html')


def signin(request):
    # return HttpResponseRedirect('login.html')
    return render(request, 'login.html')
