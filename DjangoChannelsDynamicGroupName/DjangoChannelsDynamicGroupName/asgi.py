import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import DjangoChannelsWebSocketApp.routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoChannelsWebSocketProject.settings')

application = ProtocolTypeRouter({
  'http': get_asgi_application(),
  'websocket': URLRouter(
    DjangoChannelsWebSocketApp.routing.websocket_urlpatterns
  )
})