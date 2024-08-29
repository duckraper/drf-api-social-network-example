from django.contrib.auth.views import LogoutView
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import MyTokenObtainPairView, LogoutView

urlpatterns = [
    path('token/', include([
        path('get', MyTokenObtainPairView.as_view(), name='token-obtain'),
        path('refresh', TokenRefreshView.as_view(), name='token-refresh'),
    ])),
    path('logout', LogoutView.as_view(), name='logout-user'),
]
