from django.urls import path
from core import consumers

websocket_urlpatterns = [
    path('ws/connect/', consumers.Consumer.as_asgi()),
]
