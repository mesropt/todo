from rest_framework import mixins, viewsets
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer

from .models import User
from .pagination import UserLimitOffsetPagination
from .serializers import UserModelSerializer


class UserCustomViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    pagination_class = UserLimitOffsetPagination
