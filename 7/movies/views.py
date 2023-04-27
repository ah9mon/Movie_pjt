from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Actor, Movie, Review 
from .serializers import ActorslistSerializer, ActorsdetailSerializer, MovieslistSerializer, MoviesdetailSerializer,ReviewlistSerializer,ReviewdetailSerializer, ReviewSerializer
from rest_framework import status
# Create your views here.

@api_view(['GET'])
def actor_list(request):
    actors = Actor.objects.all()
    serializer = ActorslistSerializer(actors, many = True)
    # print(serializer)
    return Response(serializer.data)

@api_view(['GET'])
def actor_detail(request, actor_pk):
    actor = Actor.objects.get(pk = actor_pk)
    serializer = ActorsdetailSerializer(actor)
    return Response(serializer.data)

@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieslistSerializer(movies, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = Movie.objects.get(pk = movie_pk)
    serializer = MoviesdetailSerializer(movie)
    return Response(serializer.data)

@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewlistSerializer(reviews, many = True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_pk):
    review = Review.objects.get(pk = review_pk)
    if request.method == 'GET':
        serializer = ReviewdetailSerializer(review)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data) 
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def create_review(request, movie_pk):
    movie = Movie.objects.get(pk = movie_pk)
    print(movie)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie = movie)
        return Response(serializer.data)

    