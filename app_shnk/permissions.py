from rest_framework.permissions import BasePermission


class IsSuperUserOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return request.method == 'GET'