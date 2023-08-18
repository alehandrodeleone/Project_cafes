from rest_framework.permissions import BasePermission
#разделение прав доступа

class ownerPermissions(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':#ЕСЛИ МЕТОД GET ПРОСМОТР ДОСТУПЕН БЕЗ АВТОРИЗАЦИИ
            return True
        return request.user == obj.owner_cafe#если авторизованый юзер совпадает с записью в модели то ок