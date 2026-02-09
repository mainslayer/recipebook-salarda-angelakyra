from django.urls import path

from .views import * 

urlpatterns = [
    path('', home, name='home'),
    path('recipes/list/', recipes, name='recipes'),
]

app_name = 'ledger'