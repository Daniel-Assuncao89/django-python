from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Daniel Assuncao',
    })


def recipe(request, id_recipe):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'name': 'Daniel Assuncao',
    })
