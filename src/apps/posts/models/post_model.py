from django.db import models as m
from django.utils.translation import gettext_lazy as _
from apps.posts.models.base_content_model import BaseContentModel


class Post(BaseContentModel):
    image = m.ImageField(upload_to='posts/',
                         help_text=_('Upload an image for the post to get in context'),
                         blank=True,
                         null=True)

    class Meta:
        db_table = 'post'
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ['-created_at']

    def __str__(self):
        content_length = len(self.content)
        part_length = content_length * 30 // 100
        start_content = self.content[:part_length]
        end_content = self.content[-part_length:]

        return f'"{start_content}...{end_content}" by @{self.user.username}'
