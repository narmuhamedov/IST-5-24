from django.urls import path
from . import views

urlpatterns = [
    path('rezka_film_list/', views.RezkaListView.as_view(), name='rezka'),
    path('form_parser/', views.RezkaFormView.as_view(), name='form_rez'),
]