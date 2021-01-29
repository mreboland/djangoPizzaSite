from django.urls import path

from . import views

app_name = "pizza"

urlpatterns = [
    # Home page
    path("", views.index, name="index"),
    
    # Pizzas link
    path("pizzas/", views.pizzas, name="pizzas"),
    
    # Link to individual pizza toppings
    path("pizzas/<int:toppingId>/", views.toppings, name="toppings")
]
