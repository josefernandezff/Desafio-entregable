from difflib import restore
from urllib import request
from django.shortcuts import render

from home.models import Family, Friend  

def familia (request):
    family = Family.objects.all()

    context_dict = {"family": family}

    return render(
        request=request,
        context=context_dict,
        template_name="home/family_list.html", 
)

def amigo (request):
    friend = Friend.objects.all()

    context_dict = {"friend": friend}

    return render(
        request=request,
        context=context_dict,
        template_name="home/friend_list.html", 
)