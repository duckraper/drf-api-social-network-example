from django.db import models as m


class Tag(m.Model):
    posts = m.ManyToManyField(to='posts.Post', related_name='tags')
    tag = m.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'tag'
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

    def __str__(self):
        return self.tag
