from django.contrib.auth.models import User
from django import forms

from plannit.models import events
from plannit.models import schedules    

class regForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

class scheduleForm(forms.ModelForm):
    class Meta:
        model = schedules
        fields = ['owner', 'place', 'date'] 

class eventForm(forms.ModelForm):
    class Meta:
        model = events
        fields = ['schedule', 'start', 'end', 'title', 'location']

