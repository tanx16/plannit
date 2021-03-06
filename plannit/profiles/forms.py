from django.contrib.auth.models import User
from django import forms
from .models import person
from .models import login
from .models import events
from .models import schedules
from cities_light.models import City as Cities
from dal import autocomplete

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = login
        fields = ['username', 'password']

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
        fields = ['first_name', 'last_name', 'email', 'bio', 'hometown']

class scheduleForm(forms.ModelForm):
    city= forms.ModelChoiceField(
        queryset=Cities.objects.all(),
        widget=autocomplete.ModelSelect2(url='city-autocomplete')
    )
    class Meta:
        model = schedules
        fields = ['place', 'title', 'city']

class eventForm(forms.ModelForm):
    class Meta:
        model = events
        fields = ['start', 'end', 'title', 'location', 'description']
