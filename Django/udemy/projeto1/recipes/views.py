from django.shortcuts import render
from utils.recipes.factory import make_recipe
from .models import Recipe
# Create your views here.


def home(request):
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request, id_category):
    category = Recipe.objects.filter(category__id=id_category).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': category,
    })


def recipe(request, id_recipe):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True
    })
