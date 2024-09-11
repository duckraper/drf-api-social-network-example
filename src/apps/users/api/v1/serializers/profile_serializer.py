from rest_framework import serializers as s

from apps.users.models import Profile
from apps.users.validators import NationalityValidator


# TODO hacer un forgot password
class ProfileSerializer(s.ModelSerializer):
    class Meta:
        model = Profile
        exclude = [
            'user'
        ]

    def validate(self, attrs):
        if 'nationality' in attrs:
            nationality = attrs['nationality'].title()
            attrs['nationality'] = nationality
            validator = NationalityValidator()
            validator.validate(nationality)

        return super().validate(attrs)
