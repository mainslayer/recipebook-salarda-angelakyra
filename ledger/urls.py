from django.urls import path
from .views import * 

urlpatterns = [
    path('', home, name='home'),
    path('recipes/list/', recipes, name='recipes'),
    path('recipe/1/', recipe1, name='recipe1'),
    path('recipe/2/', recipe2, name='recipe2'),
]

app_name = 'ledger'