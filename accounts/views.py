from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from .serializers import CMSUserSerializer

User = get_user_model()


class CreateAuthor(CreateAPIView):
    serializer_class = CMSUserSerializer
    queryset = User.objects.all()


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'is_admin_user': user.is_admin_user,
            'full_name': user.get_full_name()
        })

    def delete(self, request, *args, **kwargs):
        if not request.user.is_anonymous and request.user.auth_token:
            request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
