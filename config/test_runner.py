"""Custom test runner that ensures the test database is properly set up."""
from django.test.runner import DiscoverRunner

class CustomTestRunner(DiscoverRunner):
    def setup_databases(self, **kwargs):
        # Call parent to create the test database
        result = super().setup_databases(**kwargs)
        # Run migrations on the test database
        from django.core.management import call_command
        call_command('migrate', '--noinput', verbosity=0)
        return result
