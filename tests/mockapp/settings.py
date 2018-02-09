import os

import django


# Make filepaths relative to settings.
ROOT = os.path.dirname(os.path.abspath(__file__))


def path(*a):
    return os.path.join(ROOT, *a)


# Django
DATABASES = {
    'default': {
        'NAME': ':memory:',
        'ENGINE': 'django.db.backends.sqlite3',
    }
}
DEBUG = True
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'tidings',
    'tests',
    'tests.mockapp',
]

if django.VERSION[:2] < (1, 7):
    INSTALLED_APPS = INSTALLED_APPS + ['south']

ROOT_URLCONF = 'tests.urls'
SITE_ID = 1
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

MIDDLEWARE_CLASSES = []

# Celery
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True  # Explode loudly during tests.

# Tidings
TIDINGS_FROM_ADDRESS = 'nobody@example.com'
TIDINGS_CONFIRM_ANONYMOUS_WATCHES = True

SECRET_KEY = 'yada-yada'
