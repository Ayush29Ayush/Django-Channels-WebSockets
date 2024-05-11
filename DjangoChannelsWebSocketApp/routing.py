from django.urls import path
from . import consumers

websocket_urlpatterns = [
  path('ws/sc/', consumers.MySyncConsumer.as_asgi()),
  path('ws/ac/', consumers.MyAsyncConsumer.as_asgi()),
]

# from django.urls import re_path
# from . import consumers

# websocket_urlpatterns = [
#     re_path(r'ws/sc/', consumers.MySyncConsumer.as_asgi()),
#     re_path(r'ws/ac/', consumers.MyAsyncConsumer.as_asgi()),
# ]
