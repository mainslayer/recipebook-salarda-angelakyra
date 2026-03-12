from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Recipe  , Profile
from .forms import RecipeForm, RecipeImageForm

def recipes(request):
    recipes = Recipe.objects.all()
    ctx = {
        "recipes": recipes
    }
    return render(request, 'ledger/recipes.html', ctx)

@login_required
def recipe_create(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        form = RecipeForm(request.POST)

        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = profile
            recipe.save()

            return redirect(recipe.get_absolute_url())
        
        else:
            form = RecipeForm()

    ctx = {"form": form}
    return render(request, './ledger/recipe_form.html', ctx)

@login_required
def recipe_add_image(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    if request.method == 'POST':
        form = RecipeImageForm(request.POST)

        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = profile
            recipe.save()

            return redirect(recipe.get_absolute_url())
        
        else:
            form = RecipeImageForm()

    ctx = {"form": form, "recipe": recipe}
    return render(request, './ledger/recipe_iamge_form.html', ctx)

@login_required
def recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients = recipe.ingredients.all()

    images = recipe.image.all()
    ctx = {'name': str(recipe), 'ingredients': ingredients, 'images': images}
    return render(request, 'ledger/recipe.html', ctx)