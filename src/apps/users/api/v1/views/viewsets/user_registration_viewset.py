from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ViewSet

from apps.users.api.v1.serializers import UserRegisterSerializer


class UserRegitrationViewSet(ViewSet, CreateModelMixin, GenericAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'], url_path='register')
    def register(self, request, *args, **kwargs):
        return super().create(request, args, kwargs)
