from django.urls import path, include
from .views import UsersViewSet, UserRegitrationViewSet
from .routers import UsersCRUDRouter

router = UsersCRUDRouter(trailing_slash=False)
router.register(r'', viewset=UsersViewSet)


urlpatterns = [
    path('register', UserRegitrationViewSet.as_view({'post': 'register'}), name='register'),
    path('', include(router.urls)),
]
