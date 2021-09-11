from django.core.files.base import ContentFile
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Registration
from .forms import RegistrationForm

# Create your views here.
def home(request):
    allRecords = Registration.objects.all()
    if request.method == "POST":
        registrationForm = RegistrationForm(request.POST)
        if registrationForm.is_valid():
            registrationForm.cleaned_data
            print(registrationForm)
            registrationForm.save()
            registrationForm = RegistrationForm()
            return HttpResponseRedirect('/')
    else:
        registrationForm = RegistrationForm()

    context = {
        'registrationForm' : registrationForm,
        "allRecords" : allRecords
    }

    return render(request, 'index.html', context)


def delete(request, id):
    deleteRecord = Registration.objects.get(pk = id)
    deleteRecord.delete()
    return HttpResponseRedirect('/')

def update(request, id):
    if request.method == "POST":
        record = Registration.objects.get(pk = id)
        registrationUpdateForm = RegistrationForm(request.POST, instance=record)
        if registrationUpdateForm.is_valid():
            registrationUpdateForm.cleaned_data
            print(registrationUpdateForm)
            registrationUpdateForm.save()
            return redirect('/')
    else:
        record = Registration.objects.get(pk = id)
        registrationUpdateForm = RegistrationForm(instance=record)

    context = {
        'registrationUpdateForm' : registrationUpdateForm,
    }

    return render(request, 'update.html', context)
