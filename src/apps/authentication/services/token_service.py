from datetime import timedelta
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError


class ITokenService:
    def blacklist_refresh_token(self, refresh_token):
        raise NotImplementedError

    def invalidate_access_token(self, access_token):
        raise NotImplementedError


class TokenService(ITokenService):
    def blacklist_refresh_token(self, refresh_token):
        token = RefreshToken(refresh_token)
        token.blacklist()

    def invalidate_access_token(self, access_token):
        try:
            AccessToken(access_token).lifetime = timedelta(seconds=1)
        except InvalidToken:
            raise TokenError("Invalid access token")
