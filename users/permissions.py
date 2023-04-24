from rest_framework import permissions


class IsAdminOrPostOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        elif request.method == "POST":
            return True
