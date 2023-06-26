from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.viewsets import ModelViewSet

from api import serializers, pagination, datatools
import core.models
import core.permissions


class NewsViewSet(ModelViewSet):
    queryset = core.models.News.objects.all()
    serializer_class = serializers.News
    pagination_class = pagination.CustomPagination
    authentication_classes = (TokenAuthentication,)
    permission_classes = (core.permissions.IsAdminOrAuthor,)

    def perform_create(self, serializer: Serializer) -> None:
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'], serializer_class=None, permission_classes=None)
    def add_or_remove_like(self, request: Request, pk: int) -> Response:
        datatools.news.add_or_remove_like(news=self.get_object(), user=self.request.user)
        return Response({'Response': 'OK'})


class CommentsViewSet(ModelViewSet):
    queryset = core.models.Comments.objects.all()
    serializer_class = serializers.Comments
    pagination_class = pagination.CustomPagination
    authentication_classes = (TokenAuthentication,)
    permission_classes = (core.permissions.IsAdminOrAuthor | core.permissions.IsAboveOwner,)

    def perform_create(self, serializer: Serializer) -> None:
        serializer.save(author=self.request.user)


