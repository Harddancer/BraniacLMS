"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
=======
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
>>>>>>> 90cd3ea1ddae7f3dd5392499e5006d778f5ad2e4

application = get_wsgi_application()
