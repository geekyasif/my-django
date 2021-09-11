from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
