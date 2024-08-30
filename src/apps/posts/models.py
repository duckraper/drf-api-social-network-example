from django.db import models as m
from django.utils.translation import gettext_lazy as _


class Post(m.Model):
    user = m.ForeignKey(to='users.User', on_delete=m.CASCADE, related_name='posts')
    content = m.CharField(max_length=255)
    image = m.ImageField(upload_to='posts/',
                         help_text=_('Upload an image for the post to get in context'),
                         blank=True)
    archived = m.BooleanField(default=False)
    created_at = m.DateTimeField(auto_now_add=True)
    updated_at = m.DateTimeField()

    class Meta:
        db_table = 'post'
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return f'"{self.content[:50]}...{self.content[-50:]}" by @{self.user.username}'
