from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.serializers import DirectorSerializers, MovieSerializers, ReviewSerializers, DirectorCountSerialize
from movie_app.models import Director, Movie, Review

@api_view(['GET'])
def test(request):
    data = {
        'text': 'Hello World!',
        'int': 100,
        'float': 2.99,
        'list': [1, 2, 3],
        'bool': False,
    }
    return Response(data=data)

###------------------------GET ALL----------------------

@api_view(['GET'])
def director_list_view(request):
    director = Director.objects.all()
    serializer = DirectorSerializers(director, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def movie_list_view(request):
    movie = Movie.objects.all()
    serializer = MovieSerializers(movie, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def review_list_view(request):
    review = Review.objects.all()
    serializer = ReviewSerializers(review, many=True)
    return Response(data=serializer.data)

###---------------GET FROM ID--------------------


@api_view(['GET'])
def director_item_view(request, id):
    directors = Director.objects.get(id=id)
    serializer = DirectorCountSerialize(directors)
    return Response(data=serializer.data)

@api_view(['GET'])
def movie_item_view(request, id):
    movies = Movie.objects.get(id=id)
    serializer = MovieSerializers(movies)
    return Response(data=serializer.data)

@api_view(['GET'])
def review_item_view(request, id):
    reviews = Review.objects.get(id=id)
    serializer = ReviewSerializers(reviews)
    return Response(data=serializer.data)

@api_view(['GET'])
def movies_reviews_view(request):
    movie_reviews = Movie.objects.all()
    data = MovieSerializers(movie_reviews, many=True).data
    return Response(data=data)

