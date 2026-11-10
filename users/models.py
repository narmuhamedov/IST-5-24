from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    GENDER = (
        ('М', 'М'),
        ('Ж', 'Ж')
    )
    #first_name, last_name, email

    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=100, choices=GENDER)
    photo = models.ImageField(upload_to='users/')

    def __str__(self):
        return self.username