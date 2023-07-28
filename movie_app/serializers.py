from rest_framework import serializers
from . import models


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        fields = '__all__'


class DirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Director
        fields = ['id', 'name', 'age', 'country', 'movies_count']


class MovieSerializer(serializers.ModelSerializer):
    director = serializers.StringRelatedField()
    genres = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.Movie
        fields = ['id', 'title', 'description', 'duration', 'director', 'genres']


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


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    description = serializers.CharField()
    duration = serializers.IntegerField()
    director = serializers.IntegerField(min_value=1)
    genres = serializers.ListField(child=serializers.IntegerField(min_value=1))

    def validate_director(self, value):
        if not models.Director.objects.filter(id=value).exists():
            raise serializers.ValidationError(f"Director with id {value} does not exist.")
        return value

    def validate_genres(self, value):
        if len(value) > 5:
            raise serializers.ValidationError("A movie cannot have more than 5 genres.")
        errors = []
        for genre_id in value:
            if not models.Genre.objects.filter(id=genre_id).exists():
                errors.append(f"Genre with id {genre_id} does not exist.")
        if errors:
            raise serializers.ValidationError(errors)
        return value
