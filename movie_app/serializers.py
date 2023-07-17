from rest_framework import serializers
from . import models

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Director
        fields = '__all__'

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
