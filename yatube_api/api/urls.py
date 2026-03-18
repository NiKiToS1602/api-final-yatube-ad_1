from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register('follow', FollowViewSet, basename='follow')

comment_list = CommentViewSet.as_view({'get': 'list', 'post': 'create'})
comment_detail = CommentViewSet.as_view(
    {
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }
)

urlpatterns = [
    path('', include(router.urls)),
    path(
        'posts/<int:post_id>/comments/',
        comment_list,
        name='comment-list',
    ),
    path(
        'posts/<int:post_id>/comments/<int:pk>/',
        comment_detail,
        name='comment-detail',
    ),
    path('jwt/create/', TokenObtainPairView.as_view(), name='jwt-create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt-verify'),
]
