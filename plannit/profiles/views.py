from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View, DetailView
from .forms import regForm, UserForm, PersonForm, scheduleForm, eventForm, LoginForm
from django.contrib.auth import logout
from .models import *
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import RedirectView
from django.contrib.auth.decorators import login_required
from dal import autocomplete
from cities_light.models import City

# Create your views here.
def index(request):
    raise Http404("You've tried to access the profile root directory. Don't do this.")

def checkuser(request):
    if request.user.is_authenticated():
        print("lol")
        return HttpResponseRedirect('/profiles/' +str(request.user.person.id))
    return HttpResponseRedirect('/profiles/login')

def logged_out(request):
    return render(request, "loggedoutprofile.html", {})

def delete(request, pk, user_id):
    obj = schedules.objects.get(pk=pk)
    obj.delete()
    return HttpResponseRedirect('/profiles/' + str(user_id))

class ScheduleDelete(DeleteView):
    model = schedules
    success_url = reverse_lazy('index')
    template_name = 'delete_schedule.html'

def loadprof(request, profile_id):
    try:
        user = person.objects.get(id=profile_id)
        user_schedules = user.my_schedules.all()
    except person.DoesNotExist:
        raise Http404("The profile you are looking for does not exist.")
    if request.user.person.id == int(profile_id):
        return render(request, 'profile.html', {'curruser': request.user, 'user': user, "user_schedules": user_schedules})
    return render(request, 'profileview.html', {'curruser': request.user, 'user': user, "user_schedules": user_schedules})

def like_schedule(request):
    sched_id = None
    if request.method == 'GET':
        sched_id = request.GET['schedule_id']
        curruser_id = request.GET['current_user']
    likes = 0
    liked = "liked2.png"
    if sched_id:
        sched = schedules.objects.get(id = int(sched_id))
        curruser = person.objects.get(id = int(curruser_id))
        if curruser in sched.person_likes.all():
            liked = "notliked2.png"
            sched.likes -= 1
            sched.person_likes.remove(curruser)
        else:
            sched.likes += 1
            sched.person_likes.add(curruser)
        likes = sched.likes
        sched.save()
    return HttpResponse(str(likes) + "/" + str(liked))

class RegFormView(View):
    form_class = regForm
    template_name = 'register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit = False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            user.set_password(password)
            user.save()
            newperson = person(user=user, first_name=first_name, last_name=last_name, email=email)
            newperson.save()
            user = authenticate(username=username, password=password)
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            user.save()
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/profiles/login/')
        return render(request, self.template_name, {'form': form})

def update_person(request):
    if request.method == 'POST':
        person_form = PersonForm(request.POST, instance = request.user.person)
        if person_form.is_valid():
            person_form.save()
            return redirect("/profiles/" + str(request.user.person.id))
    else:
        person_form = PersonForm(instance = request.user.person)
    return render(request, 'newprofile.html', {'profile_form' : person_form})

#def register_view(request):
#    if request.method == "POST":
#        form = UserCreationForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect("/profiles")
#    else:
#        form = UserCreationForm()
#    return render(request, "register.html", {'form': form})

def home(request):
    return HttpResponseRedirect('/')

def logout_view(request):
    logout(request)
    return redirect('/index')

class ScheduleFormView(View):
    form_class = scheduleForm
    template_name = 'newschedule.html'
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            schedule = form.save(commit = False)
            schedule.owner = request.user.person
            schedule.save()
            return redirect("/profiles/addevent/"+ str(schedule.id))

        return render(request, self.template_name, {'form': form})

class EventFormView(DetailView):
    form_class = eventForm
    template_name = 'newevent.html'

    def get(self, request, schedule_id):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, schedule_id):
        form = self.form_class(request.POST)
        if form.is_valid():
            sid = self.kwargs['schedule_id']
            event = form.save(commit = False)
            schedule = schedules.objects.get(id=sid)
            event.schedule = schedule
            event.save()
            return render(request, self.template_name, {'form': form, 'event':schedule.events_set.all(), 'userid': schedule.owner.id})
        return render(request, self.template_name, {'form': form, 'userid':schedule.owner.id})

class CityAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return City.objects.none()

        qs = City.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs
