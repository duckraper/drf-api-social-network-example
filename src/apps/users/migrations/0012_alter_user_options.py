# Generated by Django 5.0.3 on 2024-08-27 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_user_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['username', '-date_joined'], 'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]
