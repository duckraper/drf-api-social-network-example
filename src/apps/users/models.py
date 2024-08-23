from django.db import models as m
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from core.utils.validators.phone_validator import PhoneValidator


class User(AbstractUser):
    """It's always a good idea to extend the default user model provided by Django"""

    karma = m.IntegerField(
        _("karma"),
        help_text=_(
            "Karma is a point system that rewards users for their contributions."
        ),
        default=0
    )

    class Meta:
        indexes = [
            m.Index(fields=["username"]),
            m.Index(fields=["email"]),
        ]
        ordering = [
            "username",
            "-date_joined"
        ]

    def delete(self, using=None, keep_parents=False):
        if self.pk is None:
            raise ValueError(
                "%s object can't be deleted because its %s attribute is set "
                "to None." % (self._meta.object_name, self._meta.pk.attname)
            )
        self.is_active = False
        self.save(using=using)

    def __str__(self):
        return self.username


class Profile(m.Model):
    """Sometimes profile model is used for storing additional information about the user that
    that has nothin' to do with authentication process. For automatic profile creation use signals."""

    user = m.OneToOneField(
        to=User,
        to_field="username",
        auto_created=True,
        on_delete=m.CASCADE,
        related_name="profile"
    )
    bio = m.CharField(
        _("bio"),
        max_length=255,
        help_text=_("A short description about yourself."),
        blank=True
    )
    profile_picture = m.ImageField(_("profile picture"), upload_to="profile_pics/", blank=True)
    date_of_birth = m.DateField(_("date of birth"), blank=True)
    nationality = m.CharField(_("nationality"), max_length=255, blank=True)
    phone = m.CharField(
        _("phone"),
        max_length=32,
        validators=[PhoneValidator],
        blank=True
    )
    website = m.URLField(_("website"), blank=True)
