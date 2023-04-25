from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from movies.models import Movie
from movies.permissions import IsAdminOrReadOnly
from movies.serializers import MovieSerializer
import ipdb


class MovieView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def perform_create(self, serializer):
        # ipdb.set_trace()
        serializer.save(user=self.request.user, genres=self.request.data['genres'])

    ...
