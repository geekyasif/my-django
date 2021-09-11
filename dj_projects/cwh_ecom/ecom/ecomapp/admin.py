from .models import Product
from django.contrib import admin
from django.contrib.admin.decorators import register
from django.contrib.admin.sites import site
from django.contrib import admin

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # list_display = ['product_name', 'product_name']
    prepopulated_fields = {'product_slug': ('product_name',)}
