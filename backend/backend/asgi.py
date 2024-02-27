import os

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddleweareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from backend.BasicApp.routing import ws_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddleweareStack(URLRouter(ws_urlpatterns))
})
