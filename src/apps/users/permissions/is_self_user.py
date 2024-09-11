from rest_framework.permissions import BasePermission


class IsSelfUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user


class IsOwnerUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
