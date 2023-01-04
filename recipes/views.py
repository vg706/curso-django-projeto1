from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Vinicius Gabriel',
    })


def contact(request):
    return HttpResponse('contato')


def about(request):
    return HttpResponse('sobre')
