from . import serializers
from . import models
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def directors_list_api_view(request):
    if request.method == 'GET':
        directors = models.Director.objects.prefetch_related('director_movies').all()
        serializer = serializers.DirectorSerializer(directors, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.DirectorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors)


@api_view(['GET', 'POST'])
def movies_list_api_view(request):
    if request.method == 'GET':
        movies = models.Movie.objects.select_related('director').all()
        serializer = serializers.MovieSerializer(movies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors)


@api_view(['GET', 'POST'])
def reviews_list_api_view(request):
    if request.method == 'GET':
        reviews = models.Review.objects.select_related('movie').all()
        serializer = serializers.ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def director_detail_api_view(request, pk):
    try:
        director = models.Director.objects.get(id=pk)
    except models.Director.DoesNotExist:
        return Response({'error': 'Director object does not found'}, status=404)
    if request.method == 'GET':
        serializer = serializers.DirectorSerializer(instance=director)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = serializers.DirectorSerializer(instance=director, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PATCH':
        serializer = serializers.DirectorSerializer(instance=director, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    else:
        director.delete()
        return Response(status=204)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def movie_detail_api_view(request, pk):
    try:
        movie = models.Movie.objects.get(id=pk)
    except models.Movie.DoesNotExist:
        return Response({'error': 'Movie object does not found'}, status=404)
    if request.method == 'GET':
        serializer = serializers.MovieSerializer(movie)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = serializers.MovieSerializer(instance=movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PATCH':
        serializer = serializers.MovieSerializer(instance=movie, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    else:
        movie.delete()
        return Response(status=204)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def review_detail_api_view(request, pk):
    try:
        review = models.Review.objects.get(id=pk)
    except models.Review.DoesNotExist:
        return Response({'error': 'Review object does not found'}, status=404)
    if request.method == 'GET':
        serializer = serializers.ReviewSerializer(review)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = serializers.ReviewSerializer(instance=review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PATCH':
        serializer = serializers.ReviewSerializer(instance=review, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    else:
        review.delete()
        return Response(status=204)


@api_view(['GET'])
def movies_reviews_view(request):
    movies = models.Movie.objects.select_related('director').prefetch_related('movie_reviews').all()
    serializer = serializers.MovieWithReviewsSerializer(movies, many=True)
    return Response(serializer.data)
