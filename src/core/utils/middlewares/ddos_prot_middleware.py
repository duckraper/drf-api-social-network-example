from django.http import HttpResponseForbidden
from django.core.cache import cache
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class DDoSProtectionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.time_window = 60

    def process_request(self, request):
        ip_address = request.META.get('REMOTE_ADDR')
        cache_key = f"DDoS_{ip_address}"

        request_count = cache.get(cache_key, 0)
        request_count += 1

        if request_count > settings.REQUESTS_PER_MINUTE_ALLOWED:
            return HttpResponseForbidden(_("Too many requests."))

        cache.set(cache_key, request_count, timeout=self.time_window)

        return None

    def __call__(self, request):
        return self.process_request(request) or self.get_response(request)
