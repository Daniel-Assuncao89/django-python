from django.http import Http404
from django.shortcuts import render
from utils.recipes.factory import make_recipe
from .models import Recipe
# Create your views here.


def home(request):
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request, id_category):
    recipes = Recipe.objects.filter(
        category__id=id_category,
        is_published=True,
    ).order_by('-id')

    if not recipes:
        raise Http404('Not found')

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes.first().category.name} - Category | '
    })


def recipe(request, id_recipe):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True
    })
