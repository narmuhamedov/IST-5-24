from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
from datetime import datetime

def blog_detail_view(request, id):
    if request.method == 'GET':
        blog_id = get_object_or_404(models.Blog, id=id)
    return render(request, 'blog_detail.html', {'blog_id': blog_id})

def blog_list_view(request):
    if request.method == 'GET':
        blog = models.Blog.objects.all()
    return render(request, 'blog_list.html', {'blog': blog})


def about_me(request):
    if request.method == "GET":
        about_me = {
            "name": "Радомир",
            "work": "IT Teacher",
            "hobby": "Dance",
            "time": datetime.now(),
            "phone_numbers": ['0550123321', '0999321123', '0111222333']
        }
    return render(request, 'about_me.html', {'about_me':about_me})


def contacts(request):
        return render(request,'contacts.html')