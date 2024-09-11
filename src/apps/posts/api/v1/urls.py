from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.posts.api.v1.views.viewsets import PostsViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'', PostsViewSet)

urlpatterns = [
    path(r'', include(router.urls))
]
