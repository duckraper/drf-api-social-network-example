from django.db import models as m


class Tag(m.Model):
    posts = m.ManyToManyField(to='posts.Post', related_name='tags')
    tag = m.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.tag
