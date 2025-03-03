from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
# Create your views here.

def hello (request, day):
    learn = None
    if day == "sunday":
        learn = "<h1>Learn Data Structures and Web Concept </h1>"
    elif day == "Monday":
        learn = "<h1>Learn HCI and Operations Research</h1>"
    elif day == "wednesday":
        learn ="<h1>It's a free day</h1>"
    elif day == "thursday":
        learn = "<h1>learn financial accounting</h1>"
    else:
        return HttpResponseNotFound("<h1>yayyyyyyy it's weekends!!!</h1>")
    return HttpResponse(learn)

    