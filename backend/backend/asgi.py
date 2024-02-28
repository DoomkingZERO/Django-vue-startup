import os
import sys

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from BasicApp.routing import ws_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

asgi_application = get_asgi_application()

application = ProtocolTypeRouter({
    'http': asgi_application,
    'websocket': AuthMiddlewareStack(URLRouter(ws_urlpatterns))
})
