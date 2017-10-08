from django.contrib.auth.models import User
from django import forms
from .models import person

class regForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password']

class PersonForm(forms.ModelForm):
    class Meta:
        model = person
        fields = ['name', 'bio', 'hometown']
