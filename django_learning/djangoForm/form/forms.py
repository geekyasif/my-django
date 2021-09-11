from django import forms
# import GeeksModel from models.py 
from .models import loginForm 
# Create your models here.

class registrationForm(forms.Form):
    first_Name = forms.CharField(label='Your name',max_length=100)
    last_name = forms.CharField(max_length=100)
    user_name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)

    
class loginForm(forms.ModelForm): 
    # specify the name of model to use 
    class Meta: 
        model = loginForm 
        fields = "__all__"