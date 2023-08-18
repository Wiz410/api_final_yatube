from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView

from .views import PostViewSet
from .views import GroupViewSet
from .views import FollowViewSet
from .views import CommentViewSet


v1_router = DefaultRouter()
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
jwt_patterns = [
    path(
        'jwt/create/',
        TokenObtainPairView.as_view(),
        name='jwt-create'
    ),
    path(
        'jwt/refresh/',
        TokenRefreshView.as_view(),
        name='jwt-refresh'
    ),
    path(
        'jwt/verify/',
        TokenVerifyView.as_view(),
        name='jwt-verify'
    )
]

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/', include(jwt_patterns))
]
