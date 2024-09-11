from rest_framework import serializers as s

from apps.users.api.v1.serializers import ProfileSerializer
from apps.users.models import User


class UserSerializer(s.ModelSerializer):
    profile = ProfileSerializer(many=False, read_only=False)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'date_joined',
            'profile',
        ]