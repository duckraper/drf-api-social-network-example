from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError
from apps.users.services.nationality_service import NationalityService


class NationalityValidator:
    message = _('Enter a valid nationality.')
    code = 'invalid'
    demonyms = NationalityService.load_demonyms()

    def validate(self, value):
        if value not in self.demonyms.values():
            raise ValidationError(self.message, code=self.code)

    def __call__(self, value):
        self.validate(value)
