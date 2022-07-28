"""
ASGI config for project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

import django
django.setup()

from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
# from store.custom_middleware import TokenAuthMiddleware
from django.core.asgi import get_asgi_application
import chat_app.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

application = ProtocolTypeRouter({
	"websocket": AuthMiddlewareStack(
		URLRouter(
			chat_app.routing.websocket_urlpatterns
		)
	),
})