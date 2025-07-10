from django.db import models

# Create your models here.
class Task(models.Model):

    title = models.CharField('Название задачи', max_length=200)
    description = models.TextField('Описание', blank=True, null=True)
    completed = models.BooleanField('Выполнено', default=False)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return self.title
