from django.urls import path

from pets import views

app_name = "pets"

urlpatterns = [
    path('pets/', views.pets, name="mascotas-de-la-familia"),
]