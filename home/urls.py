from django.urls import path

from home import views

app_name = "home"

urlpatterns = [
    path('family/', views.familia, name="family-list"),
    path("family/add", views.create_family, name="family-add"),
    path('friend/', views.amigo, name="friend-list"),
]