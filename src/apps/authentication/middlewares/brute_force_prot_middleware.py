from django.conf import settings
from django.core.cache import cache
from django.urls import reverse
from django.http import HttpResponseForbidden
from rest_framework.status import HTTP_200_OK
from django.utils.translation import gettext_lazy as _


class BruteForceProtectionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.path == reverse('token-obtain') and request.method == 'POST':
            ip_address = request.META.get('REMOTE_ADDR')

            cache_key = f"login_attempt_from_{ip_address}"
            login_attempts = cache.get(cache_key, 0)

            if response.status_code != HTTP_200_OK:
                cache.set(cache_key, login_attempts + 1, timeout=settings.BRUTE_FORCE_TIMEOUT)
            else:
                cache.delete(cache_key)

            if login_attempts >= settings.BRUTE_FORCE_THRESHOLD:
                return HttpResponseForbidden(
                    _(f"Exceeded login attempts, just wait {settings.BRUTE_FORCE_TIMEOUT} seconds.")
                )

        return response
