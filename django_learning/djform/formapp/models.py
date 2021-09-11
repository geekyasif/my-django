from django.db import models
from django.forms.widgets import NumberInput

# Create your models here.
class Registration(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    branch = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name