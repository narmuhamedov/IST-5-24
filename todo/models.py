from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100, verbose_name='Что планируете?')
    description = models.TextField(verbose_name='Как планируете сделать?', blank=True)
    CHEKING = (
        ('Выполнено✅', 'Выполнено✅'),
        ('В процессе⏳', 'В процессе⏳'),
        ('Не выполнено🚫', 'Не выполнено🚫')
    )
    cheking = models.CharField(max_length=100, default='Не выполнено🚫', 
                               choices=CHEKING, verbose_name='Выберите статус')
    created_at = models.DateTimeField(auto_now_add=True)
    upated_at = models.DateTimeField(auto_now=True)

    