import requests
from rest_framework import permissions


class IsAuthenticatedOnlyFeatured:
    def has_permission(self, request, view):
        return True


    def has_object_permission(self, request, view, obj):
        return obj.featured or request.user.is_authenticated


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_superuser or request.method in permissions.SAFE_METHODS