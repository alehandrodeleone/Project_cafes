from rest_framework.permissions import BasePermission


class RestaurantPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return  request.user == obj.owner_cafe#допуск если user из токена и юзер из модели совпадают

class application_doc_Permission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return  request.user == obj.user