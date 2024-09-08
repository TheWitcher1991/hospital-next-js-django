from rest_framework.throttling import SimpleRateThrottle


class BurstRateThrottle(SimpleRateThrottle):
    scope = "burst"

    def get_cache_key(self, request, view):
        if not request.user.is_authenticated:
            return self.cache_format % {"scope": self.scope, "ident": self.get_ident(request)}
        return self.cache_format % {"scope": self.scope, "ident": request.user.pk}
