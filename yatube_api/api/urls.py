from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from api.views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet

router = DefaultRouter()

router.register(
    r'posts', PostViewSet, basename='posts'
)
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)
router.register(
    r'groups', GroupViewSet
)
router.register(
    r'follow', FollowViewSet, basename='follow'
)
jwt_patterns = [
    path('v1/jwt/create/', TokenObtainPairView.as_view(), name='get_token'),
    path('v1/jwt/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('v1/jwt/verify/', TokenVerifyView.as_view(), name='verify_token'),
]

urlpatterns = [
    path('v1/', include(router.urls), name='api-root'),
    path('', include(jwt_patterns))
]
