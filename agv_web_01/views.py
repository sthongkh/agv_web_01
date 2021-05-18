from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from .mongodb import MongoDB

def index(request):
    if request.is_ajax():
        if "login" in request.GET:
            login = request.GET["login"]
            pswd = request.GET["pswd"]
            login_status = False
            login_status = MongoDB().check_user(login, pswd)
        else:
            login_status = None

        return JsonResponse({"loginstatus": login_status})

    else:
        station = MongoDB().get_all_station(4)
        queue =  MongoDB().get_queue(1)
        agvlist = MongoDB().get_agv_num()  
        return render(request, 'index.html', {'station':station, 'queue':queue, 'agvlist':agvlist})


def static_media(request):
    return render(request, 'static-media.html')


def static_css(request):
    return render(request, 'static-css.html')


def static_js(request):
    return render(request, 'static-js.html')


def bootstrap(request):
    return render(request, 'bootstrap.html')

def login(request):
    return render(request, 'login.html')