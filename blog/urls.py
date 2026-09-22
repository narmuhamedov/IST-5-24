from django.urls import path
from . import views

urlpatterns = [
    path('hello_world/', views.hello_world_view),
    path('image_django/', views.image_django_view),
    path('about_me/', views.about_me_view),
]