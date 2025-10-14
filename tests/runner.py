import os
import sys
import django
from django.conf import settings

def run_tests():
    os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings_test'
    django.setup()
    from django.test.runner import DiscoverRunner
    test_runner = DiscoverRunner(verbosity=1)
    failures = test_runner.run_tests(['tests'])
    sys.exit(bool(failures))

if __name__ == '__main__':
    run_tests()
