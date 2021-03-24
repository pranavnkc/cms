from rest_framework.permissions import BasePermission, SAFE_METHODS


class ContentPermission(BasePermission):
    """
    Allows access only to users in 'client' group
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return not request.user.is_anonymous

    def has_object_permission(self, request, view, obj):
        if request.user.is_admin_user or request.user == obj.author:
            return True
        return False
