from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Allows access only to authenticated users.
    """
    
    def has_object_permission(self, request, view, obj):

        return bool(obj.user == request.user)