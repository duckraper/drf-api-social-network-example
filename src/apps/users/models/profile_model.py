from django.db import models as m
from django.utils.translation import gettext_lazy as _
from apps.users.validators.phone_validator import PhoneValidator

GENDERS = (
    ("M", _("Male")),
    ("F", _("Female")),
    ("O", _("Other")),
    ("N", _("Prefer not to say"))
)


class Profile(m.Model):
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
