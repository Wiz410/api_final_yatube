import base64
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import CurrentUserDefault
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator
from django.core.files.base import ContentFile

from posts.models import Comment
from posts.models import Post
from posts.models import Group
from posts.models import Follow
from posts.models import User


class Base64ImageField(serializers.ImageField):
    """Декодер `Base64` в изображение."""
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)


class PostSerializer(ModelSerializer):
    """Сериализатор модели: `Post`."""
    author = SlugRelatedField(slug_field='username', read_only=True)
    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        fields = (
            'id',
            'author',
            'text',
            'pub_date',
            'image',
            'group',
        )
        model = Post


class CommentSerializer(ModelSerializer):
    """Сериализатор модели: `Comment`."""
    author = SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = (
            'id',
            'author',
            'text',
            'created',
            'post',
        )
        read_only_fields = ('post',)
        model = Comment


class GroupSerializer(ModelSerializer):
    """Сериализатор модели: `Group`."""

    class Meta:
        model = Group
        fields = (
            'id',
            'title',
            'slug',
            'description',
        )


class FollowSerializer(ModelSerializer):
    """Сериализатор модели: `Follow`."""
    user = SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=CurrentUserDefault()
    )
    following = SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
    )

    def validate(self, data):
        if self.context['request'].user == data['following']:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя!'
            )
        return data

    class Meta:
        model = Follow
        fields = (
            'user',
            'following',
        )
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message='Вы уже подписаны!'
            )
        ]
