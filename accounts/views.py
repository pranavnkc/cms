from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from .serializers import CMSUserSerializer

User = get_user_model()


class CreateAuthor(CreateAPIView):
    serializer_class = CMSUserSerializer
    queryset = User.objects.all()
