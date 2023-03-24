from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

# Create your views here.
def index(request):
    print('왜')
    movies = Movie.objects.all()
    context = {
        'movies' : movies,
    }
    return render(request, 'movies/index.html', context)
    
def create(request):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        print('<<<')
        print(form)
        if form.is_valid :
            print('>>>')
            movie = form.save()
            return redirect('movies:detail', movie.pk)
        pass
    else:
        form = MovieForm()
    context = {
        'form' : form,
    }
    return render(request, 'movies/create.html', context)

# detail pk 필요
def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie' : movie
    }
    return render(request, 'movies/detail.html', context)

# update pk 필요
def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid() :
            form.save()
            return redirect('movies:detail', pk = movie.pk)
    else:
        form = MovieForm(instance=movie)
    
    context = {
        'form' : form,
        'movie' : movie,
    }
    return render(request, 'movies/update.html', context)

# delete pk 필요 
def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('movies:index')