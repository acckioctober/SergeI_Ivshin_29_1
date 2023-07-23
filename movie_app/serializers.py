from rest_framework import serializers
from . import models


class DirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Director
        fields = ['id', 'name', 'age', 'country', 'movies_count']


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['director'] = instance.director.name  # Выводим название режиссера вместо ID
        return representation


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['movie'] = instance.movie.title  # Выводим название фильма вместо ID
        return representation


class MovieWithReviewsSerializer(serializers.ModelSerializer):
    movie_reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = models.Movie
        fields = ['title', 'description', 'duration', 'director_name', 'rating', 'movie_reviews']
