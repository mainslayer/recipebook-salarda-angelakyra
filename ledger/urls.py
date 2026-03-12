from django.urls import path
from .views import * 

urlpatterns = [
    path('recipes/list/', recipes, name='recipes'),
    path('recipe/add/', recipe_create, name='recipe-create'),
    path('recipe/<int:pk>/add_image/', recipe_add_image, name='recipe-add-image'),
    path('recipe/<int:pk>/', recipe, name='recipe'),
]

app_name = 'ledger'