from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters
from .models import Content
from .serializers import ContentSerializer
from .permissions import ContentPermission

class ContentViewSet(viewsets.ModelViewSet):
    serializer_class = ContentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'body', 'summary', 'categories']
    permission_classes = (ContentPermission, )
    
    def get_queryset(self):
        if self.request.user.is_anonymous or self.request.user.is_admin_user:
            return Content.objects.all()
        return Content.objects.filter(author=self.request.user)


