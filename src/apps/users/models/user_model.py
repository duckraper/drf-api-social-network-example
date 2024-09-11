from django.db import models as m
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


# TODO: pensar en un sistema de seguidores y seguidos
class User(AbstractUser):
    email = m.EmailField(_("email address"), unique=True, blank=False, null=False)

    class Meta:
        db_table = 'user'
        verbose_name = 'user'
        verbose_name_plural = "users"
        indexes = [
            m.Index(fields=["username"]),
            m.Index(fields=["email"]),
        ]
        ordering = [
            "username",
            "date_joined"
        ]

    @property
    def full_name(self):
        return self.first_name + self.last_name

    def delete(self, using=None, keep_parents=False):
        if self.pk is None:
            raise ValueError(
                "%s object can't be deleted because its %s attribute is set "
                "to None." % (self._meta.object_name, self._meta.pk.attname)
            )
        self.is_active = False
        self.save(using=using)

    def save(self, *args, **kwargs):
        self.email = self.email.lower()

        for field_name in ["first_name", "last_name"]:
            field = getattr(self, field_name, None)
            if field:
                setattr(self, field_name, field.title())

        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

