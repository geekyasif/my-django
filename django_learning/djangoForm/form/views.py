from django.shortcuts import render , HttpResponse
from .forms import registrationForm, loginForm
# Create your views here.
def index(request):
    context ={
        'registrationForm':registrationForm(),
        'loginForm': loginForm()
    } 
    return render(request, "index.html", context) 