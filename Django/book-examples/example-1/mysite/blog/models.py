from django.db import models
from django.utils import timezone

# Create your models here.
# Post model that will allow us to store blog posts in the database


class Post(models.Model):
    title = models.CharField(max_length=250)  # Post title
    slug = models.SlugField(max_length=250)  # Translate into a varchar column in the SQL
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
