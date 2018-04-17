"""
WSGI config for giftwiz_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys
import django
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

django.setup()


sys.path.append('/Users/jamesdix/Desktop/giftwiz-api')

sys.path.append('/Users/jamesdix/Desktop/giftwiz-api/env/lib/python2.7/site-packages')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "giftwiz_project.settings")

call_command('runcrons')

application = get_wsgi_application()
