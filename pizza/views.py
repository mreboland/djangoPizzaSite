from django.shortcuts import render

from .models import Pizza

# Create your views here.

def index(request):
    """Home page for Pizzeria"""
    return render(request, "pizza/index.html")

def pizzas(request):
    """Show all pizza types"""
    
    pizzas = Pizza.objects.order_by("dateAdded")
    context = {"pizzas": pizzas}
    
    return render(request, "pizza/pizzas.html", context)

def toppings(request, toppingId):
    """Show the toppings of a pizza"""
    
    pizza = Pizza.objects.get(id=toppingId)
    # of note, in lesson they have topic_set, the topic is the lower case of the second model (class Topic), the one that holds the topics themselves.
    toppings = pizza.topping_set.order_by("-dateAdded")
    context = {
        "pizza": pizza,
        "toppings": toppings
    }
    
    return render(request, "pizza/toppings.html", context)
    