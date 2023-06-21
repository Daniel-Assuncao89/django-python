from django.shortcuts import render, get_list_or_404, get_object_or_404
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
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=id_category,
            is_published=True,
        ).order_by('-id'))

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category | '
    })


def recipe(request, id_recipe):
    recipe = get_object_or_404(
        Recipe, pk=id_recipe, is_published=True,
    )
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True
    })
