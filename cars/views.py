from django.shortcuts import render
from . import models

def cars_list_view(request):
    if request.method == 'GET':
        car_list = models.Car.objects.all().order_by('-id')
    return render(request, template_name='car_list.html', context={'car_list': car_list})
