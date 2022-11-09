from django.shortcuts import render, HttpResponse, redirect

from datetime import datetime
from .models import Film
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def logout_(request):
    logout(request)
    return redirect('/')

def login_(request):
    context = {
        'form': UserLoginForm()
    }
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if not user:
                return redirect('/login/')
            else:
                login(request, user)
                return redirect('/')


    return render(request, 'login.html', context)


def register_(request):
    context = {
        'form': UserLoginForm()
    }
    if request.method == 'POST':
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            User.objects.create_user(username=username, password=password)
            return redirect('/login/')
        context['form'] = form

    return render(request, 'register.html', context=context)


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


def create_film(request):
    if request.method == 'GET':
        return render(request, 'create_film.html', context={
            'form': FilmForm()
        })
    elif request.method == "POST":
        form = FilmForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


def create_director(request):
    if request.method == 'GET':
        return render(request, 'create_director.html', context={
            'form': DirectorForm()
        })
    elif request.method == "POST":
        form = DirectorForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
