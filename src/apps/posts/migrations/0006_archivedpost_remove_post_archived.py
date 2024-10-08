# Generated by Django 5.0.3 on 2024-08-30 19:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_post_image_alter_post_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchivedPost',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='posts.post')),
                ('archived_at', models.DateTimeField(auto_now_add=True)),
            ],
            bases=('posts.post',),
        ),
        migrations.RemoveField(
            model_name='post',
            name='archived',
        ),
    ]
