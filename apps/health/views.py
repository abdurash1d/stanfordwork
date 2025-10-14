from django.http import JsonResponse
from django.views import View
from django.db import connection
from django.conf import settings
import redis

class HealthCheckView(View):
    def get(self, request, *args, **kwargs):
        # Check database connection
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
                db_status = True
        except Exception:
            db_status = False

        # Check Redis connection if configured
        redis_status = True
        if hasattr(settings, 'REDIS_URL'):
            try:
                r = redis.from_url(settings.REDIS_URL)
                redis_status = r.ping()
            except redis.ConnectionError:
                redis_status = False

        status_code = 200 if all([db_status, redis_status]) else 503
        
        return JsonResponse({
            'status': 'healthy' if status_code == 200 else 'unhealthy',
            'database': 'connected' if db_status else 'disconnected',
            'cache': 'connected' if redis_status else 'disconnected',
            'environment': getattr(settings, 'ENVIRONMENT', 'development'),
            'version': getattr(settings, 'VERSION', 'unknown'),
        }, status=status_code)
