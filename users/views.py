from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from users.permissions import IsAdminOrPostOnly

from .models import User
from .serializers import UserSerializer


# class UserView(APIView, PageNumberPagination):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAdminOrPostOnly]

#     def get(self, request: Request) -> Response:
#         """
#         Listagem de usuários
#         """
#         users = User.objects.all()
#         result_page = self.paginate_queryset(users, request)
#         serializer = UserSerializer(result_page, many=True)

#         return self.get_paginated_response(serializer.data)

#     def post(self, request: Request) -> Response:
#         """
#         Registro de usuários
#         """
#         serializer = UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         serializer.save()

#         return Response(serializer.data, status.HTTP_201_CREATED)


class UserView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrPostOnly]

    queryset = User.objects.all()
    serializer_class = UserSerializer
