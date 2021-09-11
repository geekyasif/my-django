from django.db import models
from datetime import datetime  
# Create your models here.

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    category = models.ForeignKey('category', related_name="post", on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    slug= models.SlugField(max_length=255)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Category'
    
    def __str__(self):
        return self.name    
