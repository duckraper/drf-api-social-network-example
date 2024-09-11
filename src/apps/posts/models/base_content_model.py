from django.contrib.contenttypes.models import ContentType
from django.db import models as m
from apps.posts.models.vote_model import Vote
from uuid import uuid4


class BaseContentModel(m.Model):
    """Abstract base content model, may be inherited by any content model like posts, or comments"""
    id = m.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = m.ForeignKey(to='users.User',
                        on_delete=m.CASCADE,
                        related_name='%(class)ss')
    content = m.CharField(max_length=255)
    created_at = m.DateTimeField(auto_now_add=True)
    updated_at = m.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def get_content_type(self):
        return ContentType.objects.get_for_model(self)

    @property
    def downvotes(self):
        return Vote.objects.all().filter(content_type=self.get_content_type(), object_id=self.pk, value__lt=0).count()

    @property
    def upvotes(self):
        return Vote.objects.all().filter(content_type=self.get_content_type(), object_id=self.pk, value__gt=0).count()

    @property
    def absolute_votes(self):
        return self.upvotes + self.downvotes

    @property
    def voting_value(self):
        return self.upvotes - self.downvotes
