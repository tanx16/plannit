from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.auth.views import login
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

# Create your views here.
def index(request):
    raise Http404("You've tried to access the profile root directory. Don't do this.")

def checkuser(request):
    if request.user.is_authenticated():
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
        user_schedules = user.schedules_set.all()
    except person.DoesNotExist:
        raise Http404("The profile you are looking for does not exist.")
    if request.user.person.id == profile_id:
        return render(request, 'profile.html', {'user': user, "user_schedules": user_schedules})
    return render(request, 'profile.html', {'user': user, "user_schedules": user_schedules})

class LoginView(View):
    form_class = LoginForm
    template_name = 'login.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect('/profiles/' + str(user.person.id))
        return render(request, self.template_name, {'form': form})

class RegFormView(View):
    form_class = regForm
    template_name = 'register.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit = False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    login(request, user)
                    user.person.name = user.first_name + user.last_name
                    user.person.bio = "My Bio"
                    return redirect('/profiles/' + str(user.person.id))
        return render(request, self.template_name, {'form': form})

def update_person(request):
    print(request.method)
    if request.method == 'POST':
        person_form = PersonForm(request.POST, instance = request.user.person)
        if person_form.is_valid():
            person_form.save()
            return redirect("/profiles/" + str(request.user.person.id))
    else:
        print(">>>>"+str((request.user)))
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
            schedule  = form.save(commit = False)
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
            print(schedule.events_set.all())
            return render(request, self.template_name, {'form': form, 'event':schedule.events_set.all(), 'userid': schedule.owner.id})
        return render(request, self.template_name, {'form': form, 'userid':schedule.owner.id})
