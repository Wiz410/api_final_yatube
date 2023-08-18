from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.viewsets import GenericViewSet
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.mixins import ListModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from posts.models import Post
from posts.models import Group
from .serializers import PostSerializer
from .serializers import GroupSerializer
from .serializers import CommentSerializer
from .serializers import FollowSerializer
from .permissions import AuthorOrReadOnly

User = get_user_model()


def get_id(self: any) -> int:
    """Получение `id` поста.

    kwargs:
        self (any): Доступ к атрибутам класса.

    Returns:
        post_id (int): `id` поста.
    """
    return self.kwargs.get('post_id')


class PostViewSet(ModelViewSet):
    """Обработка запросов: `posts`.

    Returns:
        GET (json): Список всех постов.
        POST (json): Создание поста.
        GET PK (json): Информация о посте.
        PUT PK (json): Редактирование поста.
        PATCH PK (json): Частичное редактирование поста.
        DELETE PK (json): Удаление поста.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination
    filter_backends = (SearchFilter,)
    search_fields = ('author', 'text',)

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


class GroupViewSet(ReadOnlyModelViewSet):
    """Обработка запросов: `groups`.

    Returns:
        GET (json): Список всех групп.
        GET PK (json): Информация о группе.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(ModelViewSet):
    """Обработка запросов: `comments`.

    Returns:
        GET (json): Список всех комментариев.
        POST (json): Создание комментария.
        GET PK (json): Информация о комментарии.
        PUT PK (json): Редактирование комментария.
        PATCH PK (json): Частичное редактирование комментария.
        DELETE PK (json): Удаление комментария.
    """
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)
    filter_backends = (SearchFilter,)
    search_fields = ('text',)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=get_id(self))
        return post.comments.all()

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=get_id(self))
        return serializer.save(author=self.request.user, post=post)


class FollowViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    """Обработка запросов: `follow`.

    Reruns:
        GET (json): Список всех подписок.
        POST (json): Подписка на пользователя.
    """
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter,)
    search_fields = ('^user__username', '^following__username',)

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user.username)
        return user.user.all()

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
