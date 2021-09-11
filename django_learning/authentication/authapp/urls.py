from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name="home"),
    path('registration/', views.registration, name="registration"),
    path('login/', LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', LogoutView.as_view(template_name="logout.html")),
]
