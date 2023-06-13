from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Daniel Assuncao',
    })


def sobre(request):
    return render(request, 'temp.html')


def contato(request):
    return HttpResponse('CONTATO')
