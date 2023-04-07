
# Create your views here.
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required


@require_safe
def index(request):
    print('>>>')
    movies = Movie.objects.all()
    context = {
        'movies' : movies,
    }
    return render(request, 'movies/index.html', context)

@login_required
@require_http_methods(['GET','POST'])
def create(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk) 
    else:
        form = MovieForm()
    context = {
        "form" : form,
    }
    return render(request, 'movies/create.html', context)

@require_safe
def detail(request, pk):
    movie = Movie.objects.get(pk = pk)
    context = {
        'movie' : movie,
    }
    return render(request, 'movies/detail.html', context)

@login_required
@require_http_methods(['GET','POST'])
def update(request, pk):
    movie = Movie.objects.get(pk = pk)

    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie.pk) # replace with the name of your detail view
    else:

        form = MovieForm(instance = movie)

    context = {
        'form' : form,
        'movie' : movie,
    }

    return render(request, 'movies/update.html', context)

@login_required
@require_POST
def delete(request, pk):
    movie = Movie.objects.get(pk = pk)
    movie.delete()
    return redirect('movies:index')
