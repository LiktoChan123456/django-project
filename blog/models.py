from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = RichTextField()
    body = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)