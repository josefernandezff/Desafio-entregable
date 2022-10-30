from difflib import restore
from urllib import request
from django.shortcuts import render
### lo trae django por defecto cuando creo la app

from home.models import Family, Friend  
### importo desde los modelos la clase Family 

def familia (request):
    family = Family.objects.all()

    context_dict = {"family": family}

    return render(
        request=request,
        context=context_dict,
        template_name="home/family_list.html", ### el nombre template_name es la ruta hacia el template de la app
)

def amigo (request):
    friend = Friend.objects.all()

    context_dict = {"friend": friend}

    return render(
        request=request,
        context=context_dict,
        template_name="home/friend_list.html", ### el nombre template_name es la ruta hacia el template de la app
)