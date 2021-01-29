from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

# 18-4. Pizzeria: Start a new project called pizzeria with an app called pizzas.
# Define a model Pizza with a field called name, which will hold name values,
# such as Hawaiian and Meat Lovers. Define a model called Topping with fields
# called pizza and name. The pizza field should be a foreign key to Pizza, and
# name should be able to hold values such as pineapple, Canadian bacon, and
# sausage.
# Register both models with the admin site, and use the site to enter some
# pizza names and toppings. Use the shell to explore the data you entered.

class Pizza(models.Model):

    field = models.CharField(max_length=200)
    dateAdded = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.field


class Topping(models.Model):
    
    pizza = models.ForeignKey(Pizza, on_delete=CASCADE)
    name = models.TextField()
    dateAdded = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Toppings"
        
    def __str__(self):
        return f"{self.name}"