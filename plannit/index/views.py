from django.shortcuts import render

# Create your views here.

#TODO: have it say "Hello, Yourname" up at the top
def index(request):
    return render(request, 'index.html', {})
