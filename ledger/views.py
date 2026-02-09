from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome!")

def recipes(request):
    return render(request, 'ledger/recipes.html')

def recipe1(request):
    return render(request, 'ledger/recipe1.html')

def recipe2(request):
    return render(request, 'ledger/recipe2.html')