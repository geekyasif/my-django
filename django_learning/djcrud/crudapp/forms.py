from django import forms
from django.forms import fields, widgets
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = "__all__"
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control'}),
            'password' : forms.PasswordInput(render_value = True, attrs={'class': 'form-control', 'type':'show'})
        }