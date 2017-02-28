"""
WSGI config for eclipse project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os, sys

# Project path
sys.path.append('/var/www/eclipse/eclipse')
# Env path
sys.path.append('/var/www/eclipse/eclipseenv/lib/python2.7/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eclipse.settings")

application = get_wsgi_application()
