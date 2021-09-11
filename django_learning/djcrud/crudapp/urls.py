from django.urls import path
from crudapp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:id>', views.delete, name="delete"),
    path('updateform/<int:id>/', views.update, name="update"),
 
]
