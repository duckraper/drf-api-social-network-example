from django.db import models as m
from django.utils.translation import gettext_lazy as _
from .base_content_model import BaseContentModel


class Comment(BaseContentModel):
    post = m.ForeignKey(to='posts.Post', on_delete=m.CASCADE, related_name='comments')
    pinned = m.BooleanField(default=False)
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

    class Meta:
        db_table = 'comment'
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
        ordering = [
            'pinned',
            '-created_at'
        ]

    def __str__(self):
        return f'@{self.user.username}\'s comment on {self.post}'

    @property
    def is_reply(self):
        return self.parent is not None
