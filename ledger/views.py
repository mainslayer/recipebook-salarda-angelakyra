from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe

def recipes(request):
    recipes = Recipe.objects.all()
    ctx = {
        "recipes": recipes
    }
    return render(request, 'ledger/recipes.html', ctx)

def recipe(request, name):
    recipe = Recipe.objects.get(name=name)
    ingredients = recipe.ingredients.all()
    ctx = {'name': str(recipe), 'ingredients': ingredients}
    return render(request, 'ledger/recipe.html', ctx)