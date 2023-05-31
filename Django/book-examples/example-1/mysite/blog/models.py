from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
# Post model that will allow us to store blog posts in the database


class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)  # Post title
    slug = models.SlugField(max_length=250)  # Translate into a varchar column in the SQL
    author = models.ForeignKey(User,         # Criando uma relação many-to-one
                               on_delete=models.CASCADE,  # Vai deletar tudo que estiver relacionado ao author
                               related_name='blog_posts')  # Especificar a relação reversa de User to Post
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT
                              )

    class Meta:  # Metadata
        ordering = ['-publish']  # Define a default order (newest to oldest)
        indexes = [
            # Improve performance for queries filtering or ordering results by this field
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title

