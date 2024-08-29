from django.db import models as m
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from apps.users.validators.phone_validator import PhoneValidator

GENDERS = (
    ("M", _("Male")),
    ("F", _("Female")),
    ("O", _("Other")),
    ("N", _("Prefer not to say"))
)

# TODO: pensar en un sistema de seguidores y seguidos
class User(AbstractUser):
    """It's always a good idea to extend the default user model provided by Django"""
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


class Profile(m.Model):
    """Sometimes profile model is used for storing additional information about the user that
    that has nothin' to do with authentication process. For automatic profile creation use signals."""
    user = m.OneToOneField(
        db_column="username",
        to='users.User',
        to_field="username",
        primary_key=True,
        auto_created=True,
        on_delete=m.CASCADE,
        related_name="profile",
    )
    public = m.BooleanField(_("public"), default=True)
    karma = m.IntegerField(
        _("karma"),
        help_text=_(
            "Karma is a point system that rewards users for their contributions."
        ),
        default=0
    )
    bio = m.CharField(
        _("bio"),
        max_length=255,
        help_text=_(
            "A short description about yourself."
        ),
        blank=True,
        null=True
    )
    profile_picture = m.ImageField(
        _("profile picture"),
        upload_to="profile_pics/",
        blank=True,
        null=True
    )
    date_of_birth = m.DateField(_("date of birth"), blank=True, null=True)
    gender = m.CharField(_("gender"), max_length=32, choices=GENDERS)
    nationality = m.CharField(_("nationality"), max_length=255, blank=True, null=True)
    phone = m.CharField(
        _("phone"),
        max_length=32,
        validators=[PhoneValidator],
        blank=True,
        null=True
    )
    alias = m.CharField(_("alias"),max_length=64, blank=True, null=True)
    website = m.URLField(_("website"), blank=True, null=True)

    class Meta:
        db_table="user_profile"
        verbose_name="profile"

    def __str__(self):
        return "%s's profile" % self.user.username
