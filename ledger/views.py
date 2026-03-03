from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Recipe

def recipes(request):
    recipes = Recipe.objects.all()
    ctx = {
        "recipes": recipes
    }
    return render(request, 'ledger/recipes.html', ctx)

@login_required
def recipe(request, name):
    recipe = Recipe.objects.get(name=name)
    ingredients = recipe.ingredients.all()
    ctx = {'name': str(recipe), 'ingredients': ingredients,
           'author': recipe.author.name}
    return render(request, 'ledger/recipe.html', ctx)