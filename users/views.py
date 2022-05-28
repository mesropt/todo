from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet

from .filters import UserFilter
from .models import User
from .serializers import UserModelSerializer


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]