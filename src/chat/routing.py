from django.urls import path

from . import consumers

webscocket_urlpatters = [
    path("ws/<str:room_name>/", consumers.ChatConsumer.as_asgi()),
]
