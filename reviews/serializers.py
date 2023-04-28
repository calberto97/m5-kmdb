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

    class Meta:
        model = Review
        fields = ["id", "stars", "review", "critic", "spoilers", "movie_id"]
        depth = 1
