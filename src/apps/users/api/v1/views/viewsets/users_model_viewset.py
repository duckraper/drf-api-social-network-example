from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from apps.users.api.v1.serializers import UserSerializer
from apps.users.models import User


class UsersViewSet(ModelViewSet):
    queryset = User.objects.all().filter(is_active=True,
                                         is_staff=False,
                                         is_superuser=False,
                                         profile__public=True)
    serializer_class = UserSerializer
    lookup_field = 'username'
    filter_backends = [SearchFilter]
    search_fields = ['username',
                     'first_name',
                     'last_name']
