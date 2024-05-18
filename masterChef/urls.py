from django.urls import path
from masterChef.views import Home, Ingredients

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("ingredients/", Ingredients.as_view(), name="ingredients"),
]
