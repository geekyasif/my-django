from django.contrib import admin
from .models import Post, Category

# Register your models here.
# admin.site.register(Post)
admin.site.register(Category)

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinymce.js',)