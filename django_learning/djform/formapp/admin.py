from django.contrib import admin
from .models import Registration
# Register your models here.
@admin.register(Registration)
class RegisterationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'branch', 'phone']
    
