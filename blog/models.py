from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='укажите название блога')
    description = models.TextField(verbose_name='укажите описание блога')
    image = models.ImageField(upload_to='blog/', null=True, verbose_name='загрузите фото')
    created_at = models.DateField(auto_now_add=True, null=True)
    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'

