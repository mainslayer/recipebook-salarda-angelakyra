from django.db import models
from datetime import datetime
from django.urls import reverse

# Create your models here.

class Ingredient (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse('ledger:ingredient', args=[str(self.name)])
    
class Recipe (models.Model):
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse('ledger:recipe', args=[str(self.name)])
    
class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ingredient} - {self.quantity}"
