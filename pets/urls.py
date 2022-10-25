from django.urls import path
### nose para que se hace esto

from pets import views
### tengo que importar desde la app (incluso si estoy en las url de la misma app) las views

app_name = "pets"
### nose para que se hace esto, mismo nombre de la app por buena practica
urlpatterns = [
    path('pets/', views.pets, name="mascotas-de-la-familia"),
]
### "familia" es solo el nombre de la ruta, siempre termina con /,
### lo pongo en español solo para guiarme que relacion tiene, pero deberia ir en ingles
### como ya importe las views tengo que llamar a la funcion que voy a usar
### nose para que se le pone el nombre