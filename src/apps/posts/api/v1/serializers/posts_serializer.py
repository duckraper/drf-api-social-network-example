from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer, StringRelatedField
from apps.posts.models import Post


class PostsSerializer(ModelSerializer):
    # TODO: chequear la clase serializadora, quiero que en read_only me devuelva el username del usuario
    #       lo que pasa es que no puedo poner StringRelatedField, xq sino el serializador se parte, mi punto es que fokiu
    #        me aburri ya, chaos
    user = StringRelatedField(read_only=True)

    class Meta:
        model = Post
        exclude = [
            'created_at',
            'updated_at'
        ]
