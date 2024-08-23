from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

schema_view = get_schema_view(
    openapi.Info(
        title="Social Network API",
        default_version='v1',
        contact=openapi.Contact(email="klyman047@gmail.com"),
        license=openapi.License(name="Apache 2.0 License")
    ),
    public=True,
    permission_classes=[AllowAny],
    authentication_classes=[JWTAuthentication],
)
