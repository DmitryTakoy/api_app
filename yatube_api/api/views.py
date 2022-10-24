# TODO:  Напишите свой вариант
from rest_framework import viewsets, filters, permissions
from rest_framework.pagination import LimitOffsetPagination
from django.db.models import Prefetch

from posts.models import Post, Follow, Group, Comment
from .permissions import AuthorOrReadOnly, ReadOnly
from .serializers import (
    PostSerializer, CommentSerializer, GroupSerializer, FollowingsSerializer
)


class PostViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        pss = self.kwargs.get('post_id')
        qs = Post.objects.select_related(
            'group', 'author'
        ).prefetch_related(
            Prefetch('comments', queryset=Comment.objects.filter(post=pss))
        )
        return qs
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def get_permissions(self):
        if self.action == 'retrieve':
            return (ReadOnly(),)
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        return super().perform_update(serializer)

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)

    def get_permissions(self):
        if self.action == 'retrieve':
            return (ReadOnly(),)
        return super().get_permissions()

    def get_queryset(self):
        qs = Comment.objects.filter(
            post=self.kwargs.get('post_id')
        ).select_related('author')
        return qs

    def perform_create(self, serializer):
        serializer.save(
            post=Post.objects.get(id=self.kwargs.get('post_id')),
            author=self.request.user
        )

    def perform_update(self, serializer):
        return super().perform_update(serializer)

    def perform_destroy(self, serializer):
        return super().perform_destroy(serializer)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowingsSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__username', 'following__username')
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        follows = Follow.objects.filter(user=self.request.user)
        return follows

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
