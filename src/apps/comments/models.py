from django.db import models as m
from django.utils.translation import gettext_lazy as _
from apps.votes.models import Vote

class Comment(m.Model):
    post = m.ForeignKey(to='posts.Post', on_delete=m.CASCADE, related_name='comments')
    user = m.ForeignKey(to='users.User', related_name='comments', on_delete=m.CASCADE)
    content = m.CharField(max_length=255)
    parent = m.ForeignKey(
        to='self',
        null=True,
        blank=True,
        related_name='replies',
        on_delete=m.CASCADE,
        help_text=_(
          'Field for nested comments (replies), if null, means there is no reply'
        )
    )
    created_at = m.DateTimeField(auto_now_add=True)
    # TODO: preguntarle a gepeto si el auto_now aplica tambien al modifcar los valores de las foreign keys
    updated_at = m.DateTimeField(auto_now_add=True)
    pinned = m.BooleanField(default=False)

    class Meta:
        db_table = 'comment'
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
        ordering = [
            'pinned',
            'created_at'
        ]

    def __str__(self):
        return f'@{self.user.username}\'s comment on {self.post}'

    @property
    def is_reply(self):
        return self.parent is not None

    @property
    def downvotes(self):
        return Vote.objects.all().filter(comment_id=self.pk, value__lt=0).count()

    @property
    def upvotes(self):
        return Vote.objects.all().filter(comment_id=self.pk, value__gt=0).count()

    @property
    def absolute_votes(self):
        return self.upvotes + self.downvotes
