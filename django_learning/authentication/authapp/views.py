from authapp.forms import RegistrationForm
from django.http.response import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'index.html')

def registration(request):
    if request.method == "POST":
        registration = RegistrationForm(request.POST)
        if registration.is_valid():
            registration.save()
            return redirect('login')
    else:
        registration = RegistrationForm()        

    context = {
        'registration' : registration,
    }
    return render(request, 'register.html', context)