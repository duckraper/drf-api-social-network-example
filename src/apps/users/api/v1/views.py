from datetime import timedelta

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
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
    def post(request):
        access_token = request.data.get("access")
        refresh_token = request.data.get('refresh')

        if not access_token:
            return Response({"message": "Access token not provided"}, status=HTTP_400_BAD_REQUEST)
        if not refresh_token:
            return Response({"message": "Refresh token not provided"}, status=HTTP_400_BAD_REQUEST)

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()

            try:
                AccessToken(access_token).lifetime = timedelta(seconds=1)
            except InvalidToken:
                return Response({"message": "Invalid token provided"}, status=HTTP_400_BAD_REQUEST)

            return Response({"message": "Successful logout"}, status=HTTP_200_OK)

        except TokenError as e:
            return Response({"message": f"Token error: {str(e)}"}, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": f"Logout error: {str(e)}"}, status=HTTP_500_INTERNAL_SERVER_ERROR)

