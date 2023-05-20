from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django import forms

from .models import *

class ClientForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'profile-pic': forms.CheckboxInput(attrs={'class':'form-control'}),
            'change': forms.FileInput(attrs={'class':'form-control'})
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        if commit:
            user.save()
            # create a new Profile object for the new user
            profile = User.objects.create(user=user, name=user.username, email=user.email)
            profile.save()
        return user
        