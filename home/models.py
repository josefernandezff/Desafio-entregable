from unittest.util import _MAX_LENGTH
from django.db import models

class Family(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()
    job = models.CharField(max_length=40)
    studies = models.CharField(max_length=40)
    birth = models.CharField(max_length=40)

    def __str__ (self):
        return f"{self.name} - {self.last_name} - {self.job}- {self.age}"

class Friend(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()
    birth = models.CharField(max_length=40)
    ### who = models.CharField(max_length=40)
    
    def __str__ (self):
        return f"{self.name} - {self.last_name} - {self.age}"