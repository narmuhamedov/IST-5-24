from django.shortcuts import render
from django.http import HttpResponse

def hello_world_view(request):
    if request.method == 'GET':
        return HttpResponse('<h1>Привет это Джанго!</h1>')


def image_django_view(request):
    if request.method == 'GET':
        return HttpResponse('<img src="https://i.pinimg.com/736x/70/5b/bb/705bbb820c7332b04d619f7536645753.jpg" alt="image"> ')


def about_me_view(request):
    if request.method == 'GET':
        return HttpResponse("<h2>My Telegram - <a href='https://t.me/DiligensDeum' target='_blank'>Перейти</a></h2>")