from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, default='внедорожник')

    def __str__(self):
        return self.name


class Car(models.Model):
    title = models.CharField(max_length=100)
    raider = models.CharField(max_length=100, default='Иванов Иван')
    register_date = models.DateField(auto_now_add=True, null=True)
    categories = models.ManyToManyField(Category, null=True)

    def __str__(self):
        return f'{self.title}-{self.register_date}'


class NumberCar(models.Model):
    choice_car = models.OneToOneField(Car, on_delete=models.CASCADE)
    number_car = models.CharField(max_length=100, default='01KG111RUS', null=True)
    created_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.choice_car}-{self.number_car}'


class CommentCar(models.Model):
    choice_car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField(default='GOOD CAR')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.choice_car}-{self.created_at}'



