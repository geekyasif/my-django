from django.contrib.auth.models import User
from django.forms import forms, widgets
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # widgets = {
        #     # 'username': forms.TextInput(attrs={'class':'form-control'})
        #     'email': forms.EmailInput(attrs={'class':'form-control'})
        # }

class UpdateUserProfile(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login']
        labels = {'email':'Email'}

class UpdateAdminProfile(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = "__all__"
        labels = {'email':'Email'}        