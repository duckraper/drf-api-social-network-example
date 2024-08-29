# Generated by Django 5.0.3 on 2024-08-29 18:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comments', '0002_alter_comment_user'),
        ('posts', '0004_alter_post_options_alter_post_table'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(choices=[(1, 'upvote'), (-1, 'downvotes')])),
                ('comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='comments.comment')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='posts.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voted_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'vote',
                'verbose_name_plural': 'votes',
                'db_table': 'vote',
                'unique_together': {('user', 'value', 'post')},
            },
        ),
    ]
