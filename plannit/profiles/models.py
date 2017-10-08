from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    bio = models.CharField(max_length = 1000)
    hometown = models.CharField(max_length = 100)
    pic = models.ImageField()
    def __str__(self):
        return self.name

def create_person(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        newperson = person(user=user)
        newperson.save()
post_save.connect(create_person, sender = User)
#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, created, **kwargs):
#    if created:
#        person.objects.create(user = instance)

#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
#    instance.person.save()

class schedules(models.Model):
    title = models.CharField(max_length = 100, default='Untitled')
    owner = models.ForeignKey(person, on_delete=models.CASCADE)
    place = models.CharField(max_length = 100)
    date = models.DateField(auto_now_add = True)
    # TODO: Limit price to a certain range (1-5)
    price = models.PositiveIntegerField()
    public = models.BooleanField(default=0) 
    def __str__(self):
        return str(self.owner) + " - " + str(self.place) + " - " + str(self.date)

class events(models.Model):
    schedule = models.ForeignKey(schedules, on_delete=models.CASCADE)
    start = models.TimeField()
    end = models.TimeField()
    title = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    def __str__(self):
        return self.title
