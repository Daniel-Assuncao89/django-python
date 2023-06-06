from django.db import models

# Create your models here.


class Todo(models.Model):

    class Status(models.TextChoices):
        PRIORITY = 'PR', 'Priority'
        ATTENTION = 'AT', 'Attention'
        GREEN = 'GR', 'Green'

    task = models.CharField(max_length=250)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.GREEN)
