from django.urls import path
from . import views

urlpatterns = [
    path('car_list/', views.cars_list_view, name='car_list'),
]