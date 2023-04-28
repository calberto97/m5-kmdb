from rest_framework import serializers
from genres.models import Genre
from genres.serializers import GenreSerializer
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = validated_data.pop("user")
        genres = validated_data.pop("genres")
        movies = Movie.objects.create(**validated_data, user=user)

        for genre in genres:
            try:
                check = Genre.objects.get(name__iexact=genre["name"])

                check.movies.add(movies)

            except Genre.DoesNotExist:
                new_genre = Genre.objects.create(**genre)
                new_genre.movies.add(movies)

        return movies

    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "duration",
            "premiere",
            "budget",
            "overview",
            "genres",
        ]
        depth = 1
