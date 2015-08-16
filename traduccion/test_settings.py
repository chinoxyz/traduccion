import logging

from settings import *

#MIGRATION_MODULES = {"backend": "backend.migrations_not_used_in_tests"}
DATABASES['default'] =  {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'sqlite3.db'),
        'TEST_CHARSET': 'UTF8',
        'TEST_NAME': None
        }


PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)
DEBUG = False
TEMPLATE_DEBUG = False
TEST_MODE = True
logging.disable(logging.CRITICAL)

#TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
REUSE_DB=1