# Generated by Django 5.0.3 on 2024-08-28 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_remove_user_last_seen'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='alias',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='alias'),
        ),
    ]
