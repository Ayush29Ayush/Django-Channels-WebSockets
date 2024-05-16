from django.urls import path
from . import consumers_dynamic_group_name

websocket_urlpatterns = [
    path("ws/sc/", consumers_dynamic_group_name.MySyncConsumer.as_asgi()),
    path('ws/ac/', consumers_dynamic_group_name.MyAsyncConsumer.as_asgi()),
]

# from django.urls import re_path
# from . import consumers

# websocket_urlpatterns = [
#     re_path(r'ws/sc/', consumers.MySyncConsumer.as_asgi()),
#     re_path(r'ws/ac/', consumers.MyAsyncConsumer.as_asgi()),
# ]
