from django.core.management.base import BaseCommand
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
from datetime import timedelta
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

# TODO: testear q realmente funcione en el futuro
class Command(BaseCommand):
    help = _('Clean up blacklisted tokens that are older than specified time')

    def handle(self, *args, **options):
        expiration_time = timezone.now() - timedelta(days=30)
        blacklisted_tokens = BlacklistedToken.objects.filter(token__created_at__lt=expiration_time)
        count, _ = blacklisted_tokens.delete()
        self.stdout.write(self.style.SUCCESS("Succesfully deleted %s blacklisted tokens" % count))
