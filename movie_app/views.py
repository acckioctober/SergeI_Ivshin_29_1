from . import serializers
from . import models
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination


class GenreListCreateApiView(generics.ListCreateAPIView):
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer
    pagination_class = PageNumberPagination


class GenreRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer
    lookup_field = 'id'


class MovieListCreateApiView(generics.ListCreateAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    pagination_class = PageNumberPagination
    def create(self, request, *args, **kwargs):
        serializer = serializers.MovieValidateSerializer(data=request.data)
        if serializer.is_valid():
            director = models.Director.objects.get(id=serializer.validated_data['director'])
            genres = models.Genre.objects.filter(id__in=serializer.validated_data['genres'])
            movie = models.Movie.objects.create(
                title=serializer.validated_data['title'],
                description=serializer.validated_data['description'],
                duration=serializer.validated_data['duration'],
                director=director,
            )
            movie.genres.set(genres)
            return Response(serializers.MovieSerializer(movie).data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class MovieRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    lookup_field = 'id'
    def update(self, request, *args, **kwargs):
        serializer = serializers.MovieValidateSerializer(data=request.data)
        if serializer.is_valid():
            director = models.Director.objects.get(id=serializer.validated_data['director'])
            genres = models.Genre.objects.filter(id__in=serializer.validated_data['genres'])
            movie = models.Movie.objects.get(id=kwargs['id'])
            movie.title = serializer.validated_data['title']
            movie.description = serializer.validated_data['description']
            movie.duration = serializer.validated_data['duration']
            movie.director = director
            movie.genres.set(genres)
            movie.save()
            return Response(serializers.MovieSerializer(movie).data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class DirectorListCreateApiView(generics.ListCreateAPIView):
    queryset = models.Director.objects.all()
    serializer_class = serializers.DirectorSerializer
    pagination_class = PageNumberPagination


class DirectorRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Director.objects.all()
    serializer_class = serializers.DirectorSerializer
    lookup_field = 'id'


class ReviewListCreateApiView(generics.ListCreateAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    pagination_class = PageNumberPagination


class ReviewRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    lookup_field = 'id'


class MovieReviewListApiView(generics.ListAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieWithReviewsSerializer
    pagination_class = PageNumberPagination


# @api_view(['GET', 'POST'])
# def genres_list_api_view(request):
#     if request.method == 'GET':
#         genres = models.Genre.objects.all()
#         serializer = serializers.GenreSerializer(genres, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = serializers.GenreSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(status=400, data=serializer.errors)
#
#
# @api_view(['GET', 'POST'])
# def directors_list_api_view(request):
#     if request.method == 'GET':
#         directors = models.Director.objects.prefetch_related('director_movies').all()
#         serializer = serializers.DirectorSerializer(directors, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = serializers.DirectorSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(status=400, data=serializer.errors)
#
#
# @api_view(['GET', 'POST'])
# def movies_list_api_view(request):
#     if request.method == 'GET':
#         movies = models.Movie.objects.select_related('director').all()
#         serializer = serializers.MovieSerializer(movies, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = serializers.MovieValidateSerializer(data=request.data)
#         if serializer.is_valid():
#             director = models.Director.objects.get(id=serializer.validated_data['director'])
#             genres = models.Genre.objects.filter(id__in=serializer.validated_data['genres'])
#             movie = models.Movie.objects.create(
#                 title=serializer.validated_data['title'],
#                 description=serializer.validated_data['description'],
#                 duration=serializer.validated_data['duration'],
#                 director=director,
#             )
#             movie.genres.set(genres)
#             return Response(serializers.MovieSerializer(movie).data, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
#
#
# @api_view(['GET', 'POST'])
# def reviews_list_api_view(request):
#     if request.method == 'GET':
#         reviews = models.Review.objects.select_related('movie').all()
#         serializer = serializers.ReviewSerializer(reviews, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = serializers.ReviewSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(status=400, data=serializer.errors)
#
#
# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def director_detail_api_view(request, pk):
#     try:
#         director = models.Director.objects.get(id=pk)
#     except models.Director.DoesNotExist:
#         return Response({'error': 'Director object does not found'}, status=404)
#     if request.method == 'GET':
#         serializer = serializers.DirectorSerializer(instance=director)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = serializers.DirectorSerializer(instance=director, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=400, data=serializer.errors)
#     elif request.method == 'PATCH':
#         serializer = serializers.DirectorSerializer(instance=director, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=400, data=serializer.errors)
#     else:
#         director.delete()
#         return Response(status=204)
#
#
# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def movie_detail_api_view(request, pk):
#     try:
#         movie = models.Movie.objects.get(id=pk)
#     except models.Movie.DoesNotExist:
#         return Response({'error': 'Movie object does not found'}, status=404)
#     if request.method == 'GET':
#         serializer = serializers.MovieSerializer(movie)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = serializers.MovieSerializer(instance=movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=400, data=serializer.errors)
#     elif request.method == 'PATCH':
#         serializer = serializers.MovieSerializer(instance=movie, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=400, data=serializer.errors)
#     else:
#         movie.delete()
#         return Response(status=204)
#
#
# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def review_detail_api_view(request, pk):
#     try:
#         review = models.Review.objects.get(id=pk)
#     except models.Review.DoesNotExist:
#         return Response({'error': 'Review object does not found'}, status=404)
#     if request.method == 'GET':
#         serializer = serializers.ReviewSerializer(review)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = serializers.ReviewSerializer(instance=review, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=400, data=serializer.errors)
#     elif request.method == 'PATCH':
#         serializer = serializers.ReviewSerializer(instance=review, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=400, data=serializer.errors)
#     else:
#         review.delete()
#         return Response(status=204)
#
#
# @api_view(['GET'])
# def movies_reviews_view(request):
#     movies = models.Movie.objects.select_related('director').prefetch_related('movie_reviews').all()
#     serializer = serializers.MovieWithReviewsSerializer(movies, many=True)
#     return Response(serializer.data)
