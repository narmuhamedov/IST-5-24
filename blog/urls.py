from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list_view, name='main_page'),
    path('blog_list/<int:id>/', views.blog_detail_view),
    path('about_me/', views.about_me, name='about'),
    path('contacts/', views.contacts, name='cont')
]