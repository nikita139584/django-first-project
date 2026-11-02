from django.contrib import admin
from django.urls import path
from datetime import datetime
import random
from django.http import HttpResponse

def say_HelloWorld(request):

    return HttpResponse("Hello World!")

def data(request):
    day = datetime.now().weekday()
    if (day == 0):
        return HttpResponse("Понедельник")
    elif(day == 1):
        return HttpResponse("Вторник")
    elif(day == 2):
        return HttpResponse("Среда")
    elif(day == 3):
        return HttpResponse("Четверг")
    elif(day == 4):
        return HttpResponse("Пятница")
    elif(day == 5):
        return HttpResponse("Суббота")
    elif(day == 6):
        return HttpResponse("Воскресенье")
        
    return HttpResponse (day)

def citata(request):
    text = ["Я не промазал я просто не попал","Бууууу","Привет"]
    choice = random.choice(text)
    return HttpResponse (choice)
def show(request):
    hello = say_HelloWorld(request)
    day = data(request)
    text = citata(request)

    return HttpResponse(
        hello.content.decode() + "<br>" +
        day.content.decode() + "<br>" +
        text.content.decode()
    )

urlpatterns = [
    path('', show),
    
 
]