from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from apps.posts.models.post_model import Post
from apps.posts.api.v1.serializers import PostsSerializer


class PostsViewSet(ModelViewSet):
    serializer_class = PostsSerializer
    queryset = Post.objects.all().filter(user__is_active=True,
                                         user__profile__public=True)
    filter_backends = [SearchFilter]
    search_fields = ['content']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
