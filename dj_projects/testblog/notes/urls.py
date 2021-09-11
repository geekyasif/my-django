from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',  views.notesHome, name='notesHome'),
    # path('category/<category_slug>/<post_slug>', views.blogPost, name='blogPost'),
    # path('category/<cat_slug>', views.category, name='category'),
  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)