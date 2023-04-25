from rest_framework import serializers
from genres.models import Genre
from genres.serializers import GenreSerializer
from movies.models import Movie
import ipdb


class MovieSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = validated_data.pop("user")
        genres = validated_data.pop("genres")
        # ipdb.set_trace()
        movies = Movie.objects.create(**validated_data, user=user)

        for index, genre in enumerate(genres):
            try:
                check = Genre.objects.get(name__iexact=genre["name"])
                # if check:
                # print(genres[index])
                # print(check[0]['id'])
                # genres[index] = check.id
                check.movies.add(movies)
            # else:
            except Genre.DoesNotExist:
                new_genre = Genre.objects.create(**genre)
                # genres[index] = new_genre.id
                new_genre.movies.add(movies)

        # return Movie.objects.create(**validated_data, user=user, genres=genres)
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
