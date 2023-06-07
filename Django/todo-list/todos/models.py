from django.db import models


# Create your models here.


class Todo(models.Model):
    # Criar uma variavel CHOICE_STATUS. Geralmente dicionario ou tupla.
    CHOICE_STATUS = (
        ('PR', 'Priority'),
        ('AT', 'Attention'),
        ('GR', 'Green')
    )
    task = models.CharField(max_length=250, null=False, blank=False)
    status = models.CharField(max_length=2,
                              choices=CHOICE_STATUS,
                              default='GR')

    def __str__(self):
        return self.task
