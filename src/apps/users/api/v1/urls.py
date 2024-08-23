from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from .views import LogoutView


urlpatterns = [
    path('', include([
        path('auth/', include([
            path('token/', include([
                path('get', TokenObtainPairView.as_view(), name='token-obtain'),
                path('refresh', TokenRefreshView.as_view(), name='token-refresh'),
            ])),
            path('logout', LogoutView.as_view(), name='logout-user'),
        ])),
    ]))
]
