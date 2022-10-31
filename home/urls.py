from django.urls import path

from home import views

app_name = "home"

urlpatterns = [
    path('family/', views.familia, name="family-list"),
    path('friend/', views.amigo, name="friend-list"),
]