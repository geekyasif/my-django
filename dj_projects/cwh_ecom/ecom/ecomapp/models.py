from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    product_slug = models.SlugField(max_length=255, unique=True)
    product_detail = models.TextField(blank=True)
    product_image = models.ImageField(upload_to='images/', default="")
    category = models.CharField(max_length=100, default="")
    sub_category = models.CharField(max_length=100,default="")
    product_price = models.DecimalField(max_digits=10,decimal_places=2)
    created = models.DateField()

    def __str__(self):
        return self.product_name