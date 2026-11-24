from django.db import models

class RezkaModel(models.Model):
    title = models.CharField(max_length=700)
    image = models.URLField()

    def __str__(self):
        return self.title

