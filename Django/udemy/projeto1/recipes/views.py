from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.core.paginator import Paginator
from .models import Recipe
from django.contrib import messages

import os

PER_PAGES = os.environ.get('PER_PAGE', 4)


def home(request):
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('-id')

    page_obj = make_pagination(request, recipes, PER_PAGES)

    messages.success(request, 'Success')

    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
        'page_obj': page_obj,
    })


def make_pagination(request, queryset, per_page):
    paginator = Paginator(queryset, per_page)
    page_number = request.GET.get('page', 1)
    print(request.GET)
    page_obj = paginator.get_page(page_number)
    return page_obj


def category(request, id_category):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=id_category,
            is_published=True,
        ).order_by('-id'))

    page_obj = make_pagination(request, recipes, PER_PAGES)

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'page_obj': page_obj,
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
