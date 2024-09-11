from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers as s
from rest_framework.exceptions import ValidationError
from apps.users.models import User


class UserRegisterSerializer(s.ModelSerializer):
    password = s.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = s.CharField(
        write_only=True,
        required=True
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'password2'
        ]

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise ValidationError({
                'password': _("Password fields didn't match")
            }
            )
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2', None)

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password'],
        )

        return user

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                validate_password(value)
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance
