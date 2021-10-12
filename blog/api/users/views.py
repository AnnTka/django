from rest_framework import viewsets, status
from rest_framework.authtoken.admin import User
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView

from api.users.serializers import RegisterSerializer


class RegisterView(CreateAPIView, viewsets.GenericViewSet):
    serializer_class = RegisterSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create(
            username=serializer.validated_data["email"],
            email=serializer.validated_data["email"],
            password=serializer.validated_data["password"]
        )
        token, _ = Token.object.get_or_create(user=user)
        return Response(status=status.HTTP_201_CREATED, data={"token": token})
