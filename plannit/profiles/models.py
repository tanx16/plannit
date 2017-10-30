from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from cities_light.models import City
# Create your models here.
class person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    bio = models.CharField(max_length = 1000, default = "My Bio")
    email = models.CharField(max_length = 100)
    hometown = models.CharField(max_length = 100)
    pic = models.ImageField()
    def __str__(self):
        return self.first_name + self.last_name
    """
class city(models.Model):
    name = models.CharField(max_length = 100, default = "")
    country = models.CharField(max_length = 100, default = "")
    state = models.CharField(max_length = 100, default = "", blank = True)
    """
class login(models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
"""
def create_person(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        newperson = person(user=user)
        newperson.save()
post_save.connect(create_person, sender = User)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        person.objects.create(user = instance)

#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
#    instance.person.save()
"""
class schedules(models.Model):
    title = models.CharField(max_length = 100)
    owner = models.ForeignKey(person, on_delete=models.CASCADE, related_name = "my_schedules", default = "")
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name = "city_schedules", default = "")
    place = models.CharField(max_length = 100)
    date = models.DateField(auto_now_add = True)
    likes = models.IntegerField(default = 0)
    person_likes = models.ManyToManyField(person, related_name = "liked_schedules")
    # TODO: Limit price to a certain range (1-5)
    #price = models.PositiveIntegerField(default=0)
    # public = models.BooleanField(default=0)
    def __str__(self):
        return str(self.owner) + " - " + str(self.place) + " - " + str(self.date)

class events(models.Model):
    schedule = models.ForeignKey(schedules, on_delete=models.CASCADE)
    start = models.TimeField()
    end = models.TimeField()
    title = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    description = models.CharField(max_length = 10000)
    def __str__(self):
        return self.title
