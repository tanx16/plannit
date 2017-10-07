from django.db import models

# Create your models here.
class person(models.Model):
    name = models.CharField(max_length = 100)
    bio = models.CharField(max_length = 1000)
    hometown = models.CharField(max_length = 100)
    def __str__(self):
        return self.name
