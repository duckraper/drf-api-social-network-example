from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.authentication.services.token_service import TokenService
from apps.users.models import User


class MyTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        try:
            user: User = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(
                {"message": _("No active account found with the given credentials")},
                status=HTTP_400_BAD_REQUEST
            )
        print(f"{user=}")
        user.last_login = timezone.now()
        user.save()

        response = super().post(request, *args, **kwargs)
        return response


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def __init__(self, token_service=None, **kwargs):
        super().__init__(**kwargs)
        self.token_service=token_service or TokenService()

    @swagger_auto_schema(
        operation_description="Logout user",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["access", "refresh"],
            properties={
                "access": openapi.Schema(type=openapi.TYPE_STRING),
                "refresh": openapi.Schema(type=openapi.TYPE_STRING)
            }
        ),
        responses={
            200: openapi.Response("Successful logout"),
            400: openapi.Response("Bad request"),
            500: openapi.Response("Internal server error")
        }
    )
    def post(self, request):
        access_token, refresh_token = self._validate_request_data(request.data)
        if not access_token or not refresh_token:
            return Response({"message": "Tokens not provided"}, status=HTTP_400_BAD_REQUEST)

        try:
            self._perform_logout_actions(access_token, refresh_token, request.user)
            return Response({"message": "Successful logout"}, status=HTTP_200_OK)

        except TokenError as e:
            return Response({"message": f"Token error: {str(e)}"}, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": f"Logout error: {str(e)}"}, status=HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    def _validate_request_data(data):
        access_token = data.get("access")
        refresh_token = data.get('refresh')

        return access_token, refresh_token

    def _perform_logout_actions(self, access_token, refresh_token, user):
        self.token_service.blacklist_refresh_token(refresh_token)
        self.token_service.invalidate_access_token(access_token)
