from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    # title = models.CharField(max_length=200)
    # content = models.TextField(max_length=20000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)


# class Contact(models.Model):
#     name = models.CharField(max_length=25 ,default='username')
#     email = models.CharField(max_length=50)
#     phone = models.CharField(max_length=15)
#     message = models.TextField()
#     message_time = models.DateTimeField(default=datetime.now, blank=True)