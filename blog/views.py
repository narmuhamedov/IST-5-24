from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
from datetime import datetime
from django.db.models import F


def search_view(request):
     query = request.GET.get('q', '')
     if query:
          blog = models.Blog.objects.filter(title__icontains=query)
     else:
          return HttpResponse('Блог не найден!')
     return render(request, 'blog_list.html', {'blog': blog})



def blog_detail_view(request, id):
    if request.method == 'GET':
        blog_id = get_object_or_404(models.Blog, id=id)
        views_blog = request.session.get('viewed_blog', [])
        if id not in views_blog:
             blog_id.views = F('views') + 1
             blog_id.save()
             blog_id.refresh_from_db()
        views_blog.append(id)
        request.session['viewed_blog'] = views_blog
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