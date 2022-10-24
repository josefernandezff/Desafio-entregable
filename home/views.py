from difflib import restore
from urllib import request
from django.shortcuts import render
### lo trae django por defecto cuando creo la app

from home.models import Family 
### importo desde los modelos la clase Family 

def familia (request):
    family = Family.objects.all()
 
### nose de donde sale ese family

    context_dict = {"family": family}

    return render(
        request=request,
        context=context_dict,
        template_name="home/family.html", ### el nombre template_name es la ruta hacia el template de la app
)