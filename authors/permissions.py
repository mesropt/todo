from rest_framework.permissions import BasePermission


class staffOnly(BasePermission):
    def has_permission(self, request, view): # Это мы переопределяем метод
        # has_permission. Этот метод возвращает либо TRUE, либо FALSE. Тем
        # самым мы определяем доступно ли указанному пользователю эта вьюха.
        return request.user.is_staff