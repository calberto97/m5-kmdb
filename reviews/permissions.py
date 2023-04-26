from rest_framework import permissions


class IsAdminOrCritic(permissions.BasePermission):
    def has_permission(self, request, view):
        if (
            request.user.is_authenticated
            and request.user.is_superuser
            or request.user.is_authenticated
            and request.user.is_critic
        ):
            return True
        elif request.method in permissions.SAFE_METHODS:
            return True
