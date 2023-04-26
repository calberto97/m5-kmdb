from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from reviews.models import Review
from movies.models import Movie
from reviews.permissions import IsAdminOrCritic
from reviews.serializers import ReviewSerializer
import ipdb


class ReviewView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrCritic]
    pagination_class = PageNumberPagination
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        movie = get_object_or_404(Movie, id=self.kwargs.get("movie_id"))

        serializer.save(critic=self.request.user, movie=movie)

    def get_queryset(self):
        movie = get_object_or_404(Movie, id=self.kwargs.get("movie_id"))
        return Review.objects.filter(movie=movie)
