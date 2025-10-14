from .settings import *
import os

# Use in-memory SQLite database for testing
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.test.sqlite3'),
        'TEST': {
            'NAME': os.path.join(BASE_DIR, 'db.test.sqlite3'),
        },
    }
}

# Use our custom test runner
TEST_RUNNER = 'config.test_runner.CustomTestRunner'

# Disable password hashing for faster tests
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

# Disable logging during testing
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'CRITICAL',
        },
    },
}

# Disable authentication for testing
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': [],
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}

# Disable throttling for tests
REST_FRAMEWORK['DEFAULT_THROTTLE_RATES'] = {
    'anon': None,
    'user': None,
}

# Disable caching for tests
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Disable email sending
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

# Ensure migrations are run for each test to create the test database
MIGRATION_MODULES = {
    'auth': None,
    'contenttypes': None,
    'sessions': None,
    'admin': None,
    'authtoken': None,
    'axes': None,
    'sites': None,
    'account': None,
    'socialaccount': None,
    'users': None,
    'jobs': None,
    'company': None,
    'dashboard': None,
    'django_celery_results': None,
    'django_celery_beat': None,
    'token_blacklist': None,
}

# Disable password hashing for faster tests
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

# Disable caching for tests
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Disable email sending
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

# Disable async tasks for testing
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True

# Disable authentication for testing
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': [],
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}

# Disable throttling for tests
REST_FRAMEWORK['DEFAULT_THROTTLE_RATES'] = {
    'anon': None,
    'user': None,
}

# Disable logging during testing
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'null': {
            'class': 'logging.NullHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
            'level': 'CRITICAL',
        },
    },
}
