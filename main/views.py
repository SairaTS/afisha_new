from django.shortcuts import render, HttpResponse, redirect

from datetime import datetime
from .models import Film
from django.http import HttpResponse
from .forms import *
from .models import *


def index_view(request):
    return render(request, "index.html")

def date(request):
    data = {
        'date': datetime.now()
    }
    return render(request, 'datetime.html', context=data)

def film_list_view(request):
    films = {
        'films': Film.objects.all(),
    }
    return render(request, 'films.html', context=films)

def film_list_detail(request, id):
    dict_film = {}
    film_detail = Film.objects.get(id=id)
    dict_film['film_detail'] = film_detail
    return render(request, 'films_detail.html', context=dict_film)

def director_films(request, director_id):
    director = Director.objects.get(id=director_id)
    films = Film.objects.filter(director_id=director)
    context = {
        'director': director,
        'films': films
    }
    return render(request, 'director_films.html', context=context)







