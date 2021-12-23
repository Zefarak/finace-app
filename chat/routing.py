from django.urls import re_path

from . import consumers

ws_urlpatterns = [
    re_path(r'ws/(?P<ticker>\w+)/$', consumers.ChatConsumer.as_asgi()),

]