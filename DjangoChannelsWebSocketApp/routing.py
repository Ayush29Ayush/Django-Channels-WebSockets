from django.urls import path
# from . import consumers_static_group_name
# from . import consumers_dynamic_group_name
# from . import consumers_database
from . import consumers_authentication


websocket_urlpatterns = [
    path("ws/sc/<str:group_ka_naam>/", consumers_authentication.MySyncConsumer.as_asgi()),
    path('ws/ac/<str:group_ka_naam>/', consumers_authentication.MyAsyncConsumer.as_asgi()),
]

# websocket_urlpatterns = [
#     path("ws/sc/<str:group_ka_naam>/", consumers_database.MySyncConsumer.as_asgi()),
#     path('ws/ac/<str:group_ka_naam>/', consumers_database.MyAsyncConsumer.as_asgi()),
# ]

# websocket_urlpatterns = [
#     path("ws/sc/<str:group_ka_naam>/", consumers_dynamic_group_name.MySyncConsumer.as_asgi()),
#     path('ws/ac/<str:group_ka_naam>/', consumers_dynamic_group_name.MyAsyncConsumer.as_asgi()),
# ]

# websocket_urlpatterns = [
#     path("ws/sc/", consumers_static_group_name.MySyncConsumer.as_asgi()),
#     path('ws/ac/', consumers_static_group_name.MyAsyncConsumer.as_asgi()),
# ]

# from django.urls import re_path
# from . import consumers

# websocket_urlpatterns = [
#     re_path(r'ws/sc/', consumers.MySyncConsumer.as_asgi()),
#     re_path(r'ws/ac/', consumers.MyAsyncConsumer.as_asgi()),
# ]
