from django.db import models as m
from django.utils.translation import gettext_lazy as _


class Vote(m.Model):
    votes = (
        (1, 'upvote'),
        (-1, 'downvotes')
    )

    user = m.ForeignKey(to='users.User', on_delete=m.CASCADE, related_name='voted_posts')
    post = m.ForeignKey(
        to='posts.Post',
        on_delete=m.CASCADE,
        related_name='votes',
        blank=True,
        null=True
    )
    comment = m.ForeignKey(
        to='comments.Comment',
        on_delete=m.CASCADE,
        related_name='votes',
        blank=True,
        null=True
    )
    value = m.SmallIntegerField(choices=votes)

    class Meta:
        db_table = 'vote'
        verbose_name = 'vote'
        verbose_name_plural = 'votes'
        unique_together = ['user', 'value', 'post'] or ['user', 'value', 'comment']

    def save(self, *args, **kwargs):
        if self.post and self.comment:
            raise ValueError('It can not be a vote for a post and a comment at the same time')

        return super().save(*args, **kwargs)

    def __str__(self):
        return 'upvote' if self.value > 0 else 'downvote'
