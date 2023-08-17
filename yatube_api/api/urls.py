from django.urls import path
from django.urls import include
from rest_framework import routers

from .views import PostViewSet
from .views import GroupViewSet
from .views import FollowViewSet
from .views import CommentViewSet


v1_router = routers.DefaultRouter()
v1_router.register(
    r'posts',
    PostViewSet,
    basename='posts',
)
v1_router.register(
    r'groups',
    GroupViewSet,
    basename='groups',
)
v1_router.register(
    r'follow',
    FollowViewSet,
    basename='follow',
)
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments',
)

urlpatterns = [
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(v1_router.urls)),
]
