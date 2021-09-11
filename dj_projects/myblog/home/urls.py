from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('contact', views.contact, name='contact'),
   path('about', views.about, name='about'),
   path('search', views.search, name='search'),
   path('signUp_user', views.signUp_user, name='signUp_user'),
   path('login_user', views.login_user, name='login_user'),
   path('logout_user', views.logout_user, name='logout_user'),
]