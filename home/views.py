from difflib import restore
from urllib import request
from django.shortcuts import render
from datetime import datetime

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

# def get_family(request):
#     family = Family.objects.all()
#     paginator = Paginator(family, 3)
#     page_number = request.GET.get("page")
#     return paginator.get_page(page_number)
