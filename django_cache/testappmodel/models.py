from django.db import models

# Create your models here.


class Blog(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    body = models.TextField()
    # and so on
