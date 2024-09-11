from django.urls import path, include

from apps.users.api.v1.routers import UsersRouter
from apps.users.api.v1.views.viewsets import UsersViewSet, UserRegitrationViewSet

router = UsersRouter(trailing_slash=False)
router.register(r'', viewset=UsersViewSet)


urlpatterns = [
    path('register', UserRegitrationViewSet.as_view({'post': 'register'}), name='register'),
    path('', include(router.urls)),
]
