"""
WSGI config for PY_58577_Gutter_actions_urls project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PY_58577_Gutter_actions_urls.settings")

application = get_wsgi_application()
