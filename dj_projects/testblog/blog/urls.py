from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',  views.home, name='home'),
    path('category/<category_slug>/<post_slug>', views.blogPost, name='blogPost'),
    path('category/<cat_slug>', views.category, name='category'),
    # path('/category/{{post.category.slug}}/{{post.slug}}', views.categoryPost, name='categoryPost'),

]