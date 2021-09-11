from django.shortcuts import redirect, render
from django.http import request
from .forms import RegistrationForm
from .models import Registration

# Create your views here.
def home(request):
    all = Registration.objects.all()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.clean()
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            branch = form.cleaned_data['branch']
            phone = form.cleaned_data['phone']
            submit = Registration(name=name, email=email, branch=branch, phone=phone)
            submit.save()
            message = "Form submitted Successfully"
            return redirect('/', {'message' : message})
    else:
        form = RegistrationForm()
    return render(request, 'index.html', {'form':form, "all":all})
