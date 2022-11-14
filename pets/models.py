

from unittest.util import _MAX_LENGTH
from django.db import models

class Pets(models.Model):
    name = models.CharField(max_length=40)
    animal = models.CharField(max_length=40)
    race = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__ (self):
        return f"{self.name} - {self.animal} - {self.race} "

