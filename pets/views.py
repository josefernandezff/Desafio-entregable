from django.shortcuts import render
from datetime import datetime

from difflib import restore
from urllib import request


from pets.models import Pets
 

def pets (request):
    pets = Pets.objects.all()
 

    context_dict = {"pets": pets}

    return render(
        request=request,
        context=context_dict,
        template_name="pets/pets.html",
)