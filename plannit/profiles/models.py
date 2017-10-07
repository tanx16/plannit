from django.db import models

# Create your models here.
class person(models.Model):
    name = models.CharField(max_length = 100)
    bio = models.CharField(max_length = 1000)
    hometown = models.CharField(max_length = 100)
    pic = models.ImageField()
    def __str__(self):
        return self.name

class schedules(models.Model):
    user = models.ForeignKey(person, on_delete=models.CASCADE)
    place = models.CharField(max_length = 100)
    date = models.DateField(auto_now_add = True)
    def __str__(self):
        return self.date

class events(models.Model):
    start = models.TimeField()
    end = models.TimeField()
    title = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    def __str__(self):
        return self.title
