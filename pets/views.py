from django.shortcuts import render

from difflib import restore
from urllib import request

### lo trae django por defecto cuando creo la app

from pets.models import Pets
### importo desde los modelos la clase Family 

def pets (request):
    pets = Pets.objects.all()
 
### nose de donde sale ese family

    context_dict = {"pets": pets}

    return render(
        request=request,
        context=context_dict,
        template_name="pets/pets.html", ### el nombre template_name es la ruta hacia el template de la app
)