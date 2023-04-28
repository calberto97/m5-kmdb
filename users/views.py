from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from users.permissions import IsAdminOrPostOnly

from .models import User
from .serializers import UserSerializer


class UserView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrPostOnly]

    queryset = User.objects.all()
    serializer_class = UserSerializer
