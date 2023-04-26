from rest_framework import serializers
from movies.models import Movie
from users.models import User
from movies.serializers import MovieSerializer
from users.serializers import UserSerializer
from reviews.models import Review


class CriticSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name"]


class ReviewSerializer(serializers.ModelSerializer):
    critic = CriticSerializer(required=False)

    # def create(self, validated_data):
    #     movie_id = validated_data.pop("movie_id")
    #     # try:
    #     # movie = Movie.objects.get(id=movie_id)
    #     return Review.objects.create(**validated_data, movie_id=movie_id)
    # except Movie.DoesNotExist:
    # raise BaseException('aodskodiaodiasodaosdiasodaso')

    # movie = MovieSerializer()

    class Meta:
        model = Review
        fields = ["id", "stars", "review", "critic", "spoilers", "movie_id"]
        depth = 1
