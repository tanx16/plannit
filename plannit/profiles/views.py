from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    return

def loadprof(request, profile_id):
    try:
        user = person.objects.get(id=profile_id)
    except person.DoesNotExist:
        raise Http404("The profile you are looking for does not exist.")
    return render(request, 'profile.html', {'user': user})
