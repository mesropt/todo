from requests import Response
from rest_framework import mixins, viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from django.contrib.auth.models import User
from rest_framework.versioning import AcceptHeaderVersioning

from .models import User
from .pagination import UserLimitOffsetPagination
from .serializers import UserModelSerializer, UserModelSerializer0and2, UserModelSerializer0and3


class UserCustomViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet,):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    pagination_class = UserLimitOffsetPagination
    permission_classes = [IsAuthenticatedOrReadOnly]


    def get_serializer_class(self):
        if self.request.version == '0.2':
            return UserModelSerializer0and2
        if self.request.version == '0.3':
            return UserModelSerializer0and3
        return UserModelSerializer