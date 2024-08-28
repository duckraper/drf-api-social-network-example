from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.mixins import CreateModelMixin

from apps.users.api.v1.serializers import UserSerializer, UserRegisterSerializer
from apps.users.models import User


class UserRegitrationViewSet(ViewSet, CreateModelMixin, GenericAPIView):
    serializer_class = UserRegisterSerializer

    @action(detail=False, methods=['post'], url_path='register')
    def register(self, request, *args, **kwargs):
        return super().create(request, args, kwargs)


class UsersViewSet(ModelViewSet):
    queryset = User.objects.all().filter(is_active=True,
                                         is_staff=False,
                                         is_superuser=False,
                                         profile__public=True)
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'username'
    filter_backends = [SearchFilter]
    search_fields = ['username',
                     'first_name',
                     'last_name']
