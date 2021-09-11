from django import http
from django.shortcuts import redirect, render
from .forms import SignupForm, UpdateAdminProfile, UpdateUserProfile
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages 
# Create your views here.
def signup(request):
    if request.method=="POST":
        sf = SignupForm(request.POST)
        if sf.is_valid():
            sf.save()
            messages.success(request, 'Account creates successsfully')
            return HttpResponseRedirect('/login/')
    else:
        sf = SignupForm()
    return render(request, 'signup.html', {'sf':sf})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            lf = AuthenticationForm(request = request , data=request.POST)
            if lf.is_valid():
                username = lf.cleaned_data['username']
                password = lf.cleaned_data['password']
                user = authenticate(username = username, password = password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Login successfully')
                    return HttpResponseRedirect('/profile/')
        else:
            lf = AuthenticationForm()
        return render(request, 'login.html', {'lf':lf})
    else:
        return HttpResponseRedirect("/profile/")

def profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.user.is_superuser == True:
                form = UpdateAdminProfile(instance = request.user, data = request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Admin Profile updated successfully")
                    return HttpResponseRedirect('/profile/')
            else:
                form = UpdateUserProfile(instance=request.user, data = request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Profile updated successfuly')
                    return HttpResponseRedirect('/profile/')
        else:
            if request.user.is_superuser == True:
                form = UpdateAdminProfile(instance = request.user)
            else:   
                form = UpdateUserProfile(instance =request.user)        
        return render(request, "profile.html", {'form': form})
    else:
        return HttpResponseRedirect('/login/')
        

def user_logout(request):
    logout(request)
    messages.success(request, 'Logout successfully')
    return HttpResponseRedirect('/login/')

#with old passowrd
def changepassword(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user = request.user, data = request.POST)
            if fm.is_valid():
                fm.save()
                # it is used to main the user login
                update_session_auth_hash(request, fm.user)
                messages.success(request, 'Password change successfully.')
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user =request.user)
        return render(request, 'changepassword.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')
        
#without old passowrd
def newchangepassword(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = SetPasswordForm(user = request.user, data = request.POST)
            if fm.is_valid():
                fm.save()
                # it is used to main the user login
                update_session_auth_hash(request, fm.user)
                messages.success(request, 'Password change successfully.')
                return HttpResponseRedirect('/profile/')
        else:
            fm = SetPasswordForm(user =request.user)
        return render(request, 'changepassword.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')
        