from django.shortcuts import render

def index(request):
    return render(
        request=request,
        context={},
        template_name="inicio/index.html",
    )