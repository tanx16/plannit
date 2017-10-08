from django.contrib.auth.models import User
from django import forms
from .models import person

from plannit.models import events
from plannit.models import schedules    

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

class scheduleForm(forms.ModelForm):
    class Meta:
        model = schedules
        fields = ['owner', 'place', 'date'] 

class eventForm(forms.ModelForm):
    class Meta:
        model = events
        fields = ['schedule', 'start', 'end', 'title', 'location']

