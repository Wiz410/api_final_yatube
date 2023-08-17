from rest_framework.permissions import SAFE_METHODS
from rest_framework.permissions import BasePermission


class AuthorOrReadOnly(BasePermission):
    """Разрешение редактирования автором.

    Проверка метода запроса и авторизации.
    Проверка разрешения на редактирование автором объекта.

    Returns:
        has_permission (bool): True если
        метод запроса безопасный
        или пользователь авторизован.
        has_object_permission (bool): True если
        метод запроса безопасный
        или пользователь автор комментария.
    """
    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user
