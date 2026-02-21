from django.urls import path
from .views import * 

urlpatterns = [
    path('recipes/list/', recipes, name='recipes'),
    path('recipe/<str:name>/', recipe, name='recipe'),
]

app_name = 'ledger'