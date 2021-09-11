from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<str:category>/<str:sub_category>/<slug:product_slug>/', views.product_detail, name="product_detail"),
    path('checkout/', views.checkout, name="checkout"),
    path('tracker/', views.tracker, name="tracker"),
    path('search/', views.search, name="search"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),

    
]

# <str:category>/<str:sub_category>/<slug:product_slug>/
# {{products.0.category}}/{{products.0.sub_category}}/{{products.0.product_slug}}